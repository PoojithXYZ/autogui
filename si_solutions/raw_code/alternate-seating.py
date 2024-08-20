N = int(input().strip())
M = int(input().strip())
seats = input().strip()

result = "NO" if '9' in seats else "YES" if '1' in seats or (N == 1 and '0' in seats) else "NO"
print(result)