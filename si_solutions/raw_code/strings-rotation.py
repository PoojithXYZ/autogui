def is_rotation(A, B):
    if len(A) != len(B):
        return False
    concatenated = A + A
    if B in concatenated:
        return True
    else:
        return False
N = int(input().strip())
A, B = input().strip().split() 
if is_rotation(A, B):
    print("yes")
else:
    print("no")