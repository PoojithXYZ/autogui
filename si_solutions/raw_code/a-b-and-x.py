A, B, X = map(int, input().split())

absolute_diff = abs(A - B)

if absolute_diff % (2 * X) == 0:
    print("YES")
else:
    print("NO")