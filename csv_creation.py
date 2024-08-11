import csv

def read_problems(file_name):
    problems = []
    with open(file_name, 'r') as file:
        for block in file.read().split("try again"):
            lines = block.strip().splitlines()
            if lines:
                problem_name = lines[0]
                max_score = int(lines[1].split(":")[1].strip())
                problems.append((problem_name, max_score))
    return problems

def make_todo_list(problems = "chai_links.txt", done_Qs = "poo_links.txt"):
    problems_list = read_problems(problems)
    done_list = read_problems(done_Qs)
    todo_list = [problem for problem in problems_list if problem not in done_list]
    return todo_list

new_todo_list = make_todo_list()

with open('todo.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(new_todo_list)
