def sum(a,c):
    v=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] +a[j]  == b:
                v.append(i)
                v.append(j)
                
                return v
       
    return [-1,-1]
a =[2,6,5,8,11]
b =14
print(sum(a,b))
