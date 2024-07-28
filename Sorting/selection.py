def selection(arr,n):
    for i in range(n-1):
        min = i
        for j in range(i,n):
            if arr[min]>arr[j]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr
a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n = 10
print(selection(a,n))