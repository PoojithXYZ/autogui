from util_funcs import read_problems

file_chai = 'chai_links.txt'  # replace with your text file name
problems_list = read_problems(file_chai)
file_poo = 'poo_links.txt'  # replace with your text file name
done_list = read_problems(file_poo)
todo_list = [problem for problem in problems_list if problem not in done_list]

print(todo_list)
print()
print(len(todo_list))
