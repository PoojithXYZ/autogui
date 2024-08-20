import subprocess
import csv
import re
from typing import List, Tuple

from csv_creation import rewrite_name

def get_submissions(problem_link, script_path="shell_scripts/get_submissions.sh"):
    subprocess.run([script_path, problem_link])

def submission_page_from_downloads():
    subprocess.run("mv ~/Downloads/hive_file_mhtml.mhtml current_submissions_page.mhtml", shell=True)

def remove_after_fourth_multipartboundary(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    #  single_line = ''.join([line.strip() for line in lines])
    pattern = r'^(.*?(?:\r?\n--.*?multipartboundary.*?){3})'
    match = re.search(pattern, contents, re.DOTALL | re.IGNORECASE)
    if match:
        with open(file_path, 'w') as file:
            file.write(match.group(0))
    else:
        with open(file_path, 'w') as file:
            file.write(contents)

def get_links_and_scores(problem_url: str) -> List[Tuple[str, int]]:
    file_path = "current_submissions_page.mhtml"
    # [^N][^N]\d.<.td>
    replace_chars = "</td> "
    def get_scores(file_path=file_path, pattern=r'[^N][^N]\d.<.td>'):
        matches = []
        with open(file_path, 'r') as file:
            for line in file:
                match = re.search(pattern, line)
                if match: 
                    text = match.group()
                    for char in replace_chars:
                        text = text.replace(char, "")
                    matches.append(text)
        return matches
    def get_links(file_path='current_submissions_page.mhtml', pattern=r'href3D"(.*?)>'):
        links = []
        with open(file_path, 'r') as file:
            content = file.read().replace('=', '').replace('\n', '')
        matches = re.findall(pattern, content)
        for match in matches:
            if "/submission/" in match:
                links.append(match.replace('"', ''))
        return links
    list_scores = get_scores()
    list_links = get_links()
    link_score_pairs = list(zip(list_links, list_scores))
    print(link_score_pairs)
    return link_score_pairs


def choose_link(links_and_scores: List[Tuple[str, int]], max_score: int) -> str:
    max_score_links = [link for link, score in links_and_scores if score == max_score]
    if max_score_links:
        return max_score_links[0]  # Return the first link with max_score
    return max(links_and_scores, key=lambda x: x[1])[0] if links_and_scores else ''

def get_solution_to_raw_code_folder(prob_name, sol_link, script_one_path="shell_scripts/get_solution_to_raw_code_folder_one.sh", script_two_path="shell_scripts/get_solution_to_raw_code_folder_two.sh"):
    file_name = rewrite_name(prob_name)
    print(f"Downloading solution for {prob_name}...")
    subprocess.run([script_one_path, sol_link, file_name])
    #subprocess.run([script_two_path, sol_link, file_name])
    print(f"Solution saved as: si_solutions/raw_code/{file_name}.py")

if __name__ == "__main__":
    si_all_info = []
    with open('todo.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)   # skip the header row
        for row in csvreader:
            si_all_info.append(row)   # returns (name, score, link)
    for problem_info in si_all_info:
        print("----------", problem_info)
        get_submissions(problem_info[2])
        submission_page_from_downloads()
        remove_after_fourth_multipartboundary('current_submissions_page.mhtml')
        choice = choose_link(get_links_and_scores('current_submissions_page.mhtml'), max_score=int(problem_info[1]))
        print("\nchoice = ", choice)
        get_solution_to_raw_code_folder(problem_info[0], choice)

