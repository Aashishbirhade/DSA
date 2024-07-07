def rotate(n,a):
    t = a[0]
    for i in range(n-1):
        a[i] = a[i+1]
    a[n-1] = t
    for i in range(n):
        print(a[i],end = " ")

a = list(map(int,input().split()))
rotate(len(a),a)