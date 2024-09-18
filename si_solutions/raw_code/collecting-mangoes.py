class Basket:
    def __init__(self):
        self.stack = []

    def add_man(self,size):
        max_size = size if not self.stack else max(size, self.stack[-1][1])
        self.stack.append((size, max_size))

    def remove_man(self):
        if self.stack:
            self.stack.pop()

    def get_max_man(self):
        return self.stack[-1][1] if self.stack else "Empty"

s = int(input())
for case_num in range(1,s + 1):
    V = int(input())
    basket = Basket() 

    print(f"Case {case_num}:")
    for _ in range(V):
        ope = input().split()

        if ope[0] == "A":
            man_size = int(ope[1])
            basket.add_man(man_size)

        elif ope[0] == "R":
            basket.remove_man()

        elif ope[0] == "Q":
            print(basket.get_max_man())