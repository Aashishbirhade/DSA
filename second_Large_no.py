def large(a,n):
    a.sort(reverse = True)
    for i in range(1,n):
        if a[i]!=a[0]:
            return a[i]
        
            
n = int(input())
a = list(map(int,input().split()))
print("second large no is ",large(a,n))
