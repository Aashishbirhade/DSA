def multi(a):
    mul = 1
    b =[]
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]==a[j]:
                continue
            else:
                mul *= a[j]
        b.append(mul)
        mul=1
    print(b)

a =[1,2,3,4]
multi(a)