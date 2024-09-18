def rotate_ar(ar,k):
    x = len(ar)
    if x == 0 or k == 0:
        return
    k = k % x
    if k == 0:
        return 

    temp = ar[-k:] + ar[:-k]
    for i in range(x):
        ar[i] = temp[i]       

def pro_case():
    x,k = map(int, input().split())
    ar = list(map(int, input().split()))
    
    rotate_ar(ar,k)
    print(*ar)         

s = int(input()) 
for _ in range(s):
    pro_case()