N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

A = set(arr1)
B = set(arr2)

union_result = sorted(list(A.union(B)))
print(' '.join(map(str, union_result)))

intersection_result = sorted(list(A.intersection(B)))
if intersection_result:
    print(' '.join(map(str, intersection_result)))

sym_diff_result = sorted(list(A.symmetric_difference(B)))
if sym_diff_result:
    print(' '.join(map(str, sym_diff_result)))
print(str(A.isdisjoint(B)).lower())

print(str(A.issubset(B)).lower())

print(str(A.issuperset(B)).lower())