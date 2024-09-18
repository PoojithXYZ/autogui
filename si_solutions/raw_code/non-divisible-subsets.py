def lar_set(ar, n, k):
    count = [0] * k
    for i in range(n):
        count[ar[i] % k] += 1
    result = min(count[0], 1)
    if k % 2 == 0:
        result += min(count[k // 2], 1)
    for i in range(1, (k + 1) // 2):
        result += max(count[i], count[k - i])
    return result 

x = int(input())
for _ in range(x):
    n,k = map(int, input().split())
    ar = list(map(int, input().split()))
    print(lar_set(ar,n,k))