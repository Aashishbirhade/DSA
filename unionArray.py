def Union(a1,a2):
    s =set()
    v =[]
    for i in a1:
        s.add(i)
    for j in a2:
        s.add(j)
    for i in s:
        v.append(i)
    return v

a = [1,2,3,4,5]
b = [2,3,4,4,11,10,5,7]
print(Union(a,b))

#output [1, 2, 3, 4, 5, 7, 10, 11]