a = list(map(int,input().split()))
k = int(input())
v = sorted(a, reverse=True)
print(v)
for i in range(len(v)):
   if i == k:
    print(v[i-1])

# 1 2 3 4 5
# 1
# [5, 4, 3, 2, 1]
# 5