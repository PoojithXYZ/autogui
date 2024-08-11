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
