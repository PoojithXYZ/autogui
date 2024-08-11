import csv

def rewrite_name(problem_name):
    return problem_name.replace(" ", "-").replace("'", "")
 
def make_si_links(problem_name, is_basic = True):
    si_link = f"https://hive.smartinterviews.in/contests/smart-interviews-{"basic" if is_basic == True else "primary"}/problems/{rewrite_name(problem_name)}?page=0&pageSize=100"
    return si_link

def read_problems(file_name, is_basic = True):
    problems = []
    with open(file_name, 'r') as file:
        for block in file.read().split("try again"):
            lines = block.strip().splitlines()
            if lines:
                problem_name = lines[0]
                max_score = int(lines[1].split(":")[1].strip())
                problems.append((problem_name, max_score, make_si_links(problem_name, is_basic)))
    return problems

def make_todo_list(problems = "chai_links.txt", done_Qs = "poo_links.txt", is_basic = True):
    problems_list = read_problems(problems, is_basic)
    done_list = read_problems(done_Qs, is_basic)
    todo_list = [problem for problem in problems_list if problem not in done_list]
    return todo_list

if __name__ == "__main__":
    #-----------------change params here only-----------------
    new_todo_list = make_todo_list(is_basic = True)
    with open('todo.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Problem_Name", "Max_Score", "SI_Link"])
        writer.writerows(new_todo_list)

