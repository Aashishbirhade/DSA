a = list(map(int,input().split()))
li = []
for i in a:
    if i not in li:
        li.append(i)
print(li)
