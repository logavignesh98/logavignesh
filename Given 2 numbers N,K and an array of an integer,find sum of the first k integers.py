def ksum(arr,k)
    arr.sort(reverse=true)
    for i in range(k):
        print(arr[i],end=" ")
arr = [2,6,23,29,35,48,54]
k = 3
ksum(arr,k)
