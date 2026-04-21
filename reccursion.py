def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        less=[i for i in array[1:] if i<array[0]]
        more=[i for i in array[1:] if i>=array[0]]
        return quick_sort(less)+[array[0]]+quick_sort(more)

def quick_sort_sp(array):
    if len(array) <= 1:
        return array
    else:
        greater = [i for i in array[1:] if i > array[0]]
        less = [i for i in array[1:] if i <= array[0]]
        return quick_sort_sp(greater) + [array[0]] + quick_sort_sp(less)