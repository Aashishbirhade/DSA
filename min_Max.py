li = list(map(int,input().split()))
min = max = li[0]
for i in li:
    if max > i:
        max = i
    elif min < i:
        min = i
print("Max = ",max)
print("min = ", min)
