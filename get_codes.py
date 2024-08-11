import subprocess
import csv
import re
from typing import List, Tuple

from csv_creation import rewrite_name

def get_submissions(problem_link):
    commands = [
        "wmctrl -c thehive",
        f"microsoft-edge {problem_link}",
        "sleep 6",
        "xdotool mousemove 240 290 && xdotool click 1 && sleep 1 && xdotool key Ctrl+s && sleep 1",
        "wmctrl -a all files && sleep 1 && xdotool type \"hive_file_mhtml\" && xdotool key Return",
        "sleep 3 && wmctrl -c thehive"
    ]
    for command in commands:
        subprocess.run(command, shell=True)

def submission_page_from_downloads():
    subprocess.run("mv ~/Downloads/hive_file_mhtml.mhtml current_submissions_page.mhtml", shell=True)

def remove_after_fourth_multipartboundary(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    pattern = r'^(.*?(?:\r?\n--.*?multipartboundary.*?){2})'
    match = re.search(pattern, contents, re.DOTALL | re.IGNORECASE)
    if match:
        with open(file_path, 'w') as file:
            file.write(match.group(0))
    else:
        with open(file_path, 'w') as file:
            file.write(contents)

def get_links_and_scores(file_path: str) -> List[Tuple[str, int]]:
    link_score_pairs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        cleaned_content = re.sub(r'<.*?>', '', content, flags=re.DOTALL).replace('=', '')
        pattern = re.compile(r'(\d+)\s+View\s+launch', flags=re.DOTALL)
        scores = [int(match) for match in pattern.findall(cleaned_content)]
        
        pattern = r'https:\/\/hive\.smartinterviews\.in\/submission\/[a-zA-Z0-9=\r\n]*'
        links = [url.replace('=', '').replace('\n', '') for url in re.findall(pattern, content)]
        
        link_score_pairs = list(zip(links, scores))
    except IOError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return link_score_pairs

def choose_link(links_and_scores: List[Tuple[str, int]], max_score: int) -> str:
    for link, score in links_and_scores:
        if score == max_score:
            return link
    return max(links_and_scores, key=lambda x: x[1])[0] if links_and_scores else ''


def get_solution_to_raw_code_folder(prob_name, sol_link):
    file_name = rewrite_name(prob_name)
    commands = [
        f"microsoft-edge {sol_link}",
        "sleep 5",
        "wmctrl -r thehive -e \"0,945,0,990,1070\" && sleep 0.5",
        "xdotool mousemove 950 470 && xdotool click 1 && sleep 0.5",
        "xdotool key Ctrl+a && xdotool key Ctrl+c",
        f"xclip -o > solutions/raw_code/{file_name}.py"
    ]
    for command in commands:
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    si_all_info = []
    with open('todo.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)   # skip the header row
        for row in csvreader:
            si_all_info.append(row)   # returns (name, score, link)
    for problem_info in si_all_info:
        print(problem_info)
        get_submissions(problem_info[2])
        submission_page_from_downloads()
        remove_after_fourth_multipartboundary('current_submissions_page.mhtml')
        choice = choose_link(get_links_and_scores('current_submissions_page.mhtml'), max_score=int(problem_info[1]))
        print("choice = ", choice)
        get_solution_to_raw_code_folder(problem_info[0], choice)

