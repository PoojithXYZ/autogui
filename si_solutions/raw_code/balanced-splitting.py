def strings(S):
    count = 0
    balance = 0

    for char in S:
        if char == 'L':
            balance += 1
        elif char == 'R':
            balance -= 1


