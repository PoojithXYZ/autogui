class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            return "Empty"
        return self.items.pop(0)

import sys
input = sys.stdin.read
data = input().strip().split('\n') 
t = int(data[0])
queue = Queue()
results = []
for ope in data[1:t + 1]:
    if ope.startswith("Enqueue"):
        _, value = ope.split() 
        queue.enqueue(int(value))
    elif ope == "Dequeue":
        result = queue.dequeue()
        results.append(result)

for result in results:
    print(result)