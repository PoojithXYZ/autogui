class Deque:
    def __init__(self):
        self.items = []
        
    def push_front(self, item):
        self.items.insert(0, item)

    def push_back(self, item):
        self.items.append(item)

    def pop_front(self):
        if not self.items:
            return "Empty"
        return self.items.pop(0)

    def pop_back(self):
        if not self.items:
            return "Empty"
        return self.items.pop()

import sys
input = sys.stdin.read
data = input().strip().split('\n')
s = int(data[0])

deque = Deque()

results = []
for ope in data[1:s + 1]:
    parts = ope.split()
    if parts[0] == "push_front":
        value = int(parts[1])
        deque.push_front(value)
    elif parts[0] == "push_back":
        value = int(parts[1]) 
        deque.push_back(value)
    elif parts[0] == "pop_front":
        result = deque.pop_front()
        results.append(result)
    elif parts[0] == "pop_back":
        result = deque.pop_back()
        results.append(result)    

for result in results:
    print(result)
