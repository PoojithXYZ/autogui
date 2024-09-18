class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value) 

    def pop(self):
        if len(self.stack) == 0:
            return "Empty"
        else:
            return self.stack.pop()

u = int(input())
stack = Stack() 
for _ in range(u):
    ope = input().split()

    if ope[0] == "push":
        stack.push(int(ope[1]))
    elif ope[0] == "pop":
        print(stack.pop())