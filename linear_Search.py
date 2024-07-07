def Search(a,k):
    for i in range(len(a)):
        if a[i] == k:
            return i
    return -1

a = list(map(int,input().split()))
k = int(input("Enter key value "))
print("index of key is ",Search(a,k))