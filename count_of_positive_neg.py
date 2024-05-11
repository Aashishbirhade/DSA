for i in range(int(input())):
    N, k = map(int, input().split())
    A = list(map(int, input().split()))
    pos = neg = divk = i = 0
    while i<len(A):             
        #Count the negative elements of the array
        if A[i] < 0:            
            neg +=  1
        #Count the positive elements of the array
        elif A[i] > 0:          
            pos +=  1
        #Count if the given element is divisible by k
        if A[i]%k == 0:         
            divk += 1
        i +=  1
    print("positive :",pos,"negative :",neg,"Div By K :",divk)