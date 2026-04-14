def selection_sort(arr: list):
    for i in range(0,len(arr)-1):
        min_idx = min(arr[i:])
        index = arr.index(min_idx)
        arr[i],arr[index]=arr[index],arr[i]
    print(arr)
listt=[67,63,76,69,32,52,49]
selection_sort(listt)