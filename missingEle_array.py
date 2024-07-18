def Missing(a,n):
    v = n*(n+1)//2
    s = sum(a)
    return v - s
a = [1,2,4,5]
n = 5
print(Missing(a,n))