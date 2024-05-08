a = list(map(int,input().split()))
m = int(input())
c = 0
for i in range(len(a)):
  for j in range(i+1,len(a)):
    if a[i] + a[j] == m:
      c=c+1
print(c)
