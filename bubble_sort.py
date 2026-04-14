def bubble_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    print(arr)
listt=[67,63,76,69,32,52,49]
bubble_sort(listt)