li = list(map(int,input().split()))
min = max = li[0]
for i in li:
    if max >=i:
        min = i
    else:
        max = i
print("Max = ",max)
print("min = ", min)
