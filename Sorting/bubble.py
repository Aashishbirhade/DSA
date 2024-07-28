def Bubble(arr,n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] >arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

a = [3,4,1,7,9,8]
n = 6
print(Bubble(a,n))
