n,t = map(int,input().split())
l = list(map(int,input().split()))
if  t in l:
    print("yes")
else:
    print("no")
for i in l:
    if i%2 == 0:
        print("even no :- ",i)
        
