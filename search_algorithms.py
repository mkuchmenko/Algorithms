#Complexity - O(n)
def bin_search(arr:list, key:int) -> bool:
    """
    This function is used to search items in sorted array (with binary search)
    :param arr:sorted array
    :return: True if found, False otherwise
    """
    l=0
    r=len(arr)-1

    while l<=r:
        mid =(l+r)// 2
        if arr[mid]==key:
            return True

        elif arr[mid]>key:
            r=mid-1

        elif arr[mid]<key:
            l=mid+1

    return False



print(bin_search([3,4,5,6,7,8,9,10],-1))