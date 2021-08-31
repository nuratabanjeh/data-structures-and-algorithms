def quickSort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quickSort(arr, left, position - 1)
        quickSort(arr, position + 1, right)

    return arr

def partition(arr, left, right):
    pivot = arr[right]
    low = left - 1
    for i in range(left,right):
        if arr[i] <= pivot:
            low+=1
            Swap(arr, i, low)

    Swap(arr, right, low + 1)
    return low + 1

def Swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp


########TEST#########

def test_quick_sort():
    arr =[8,4,23,42,16,15]
    actual= quickSort(arr,0,len(arr)-1)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_reverse_sorted():
    arr =[20,18,12,8,5,-2]    
    actual= quickSort(arr,0,len(arr)-1)
    expected = [-2,5,8,12,18,20]
    assert actual == expected


def test_few_uniques(): 
    arr =[5,12,7,5,5,7]  
    actual= quickSort(arr,0,len(arr)-1)
    expected = [5,5,5,7,7,12]
    assert actual == expected

def test_nearly_sorted():
    arr =[2,3,5,7,13,11]   
    actual= quickSort(arr,0,len(arr)-1)
    expected = [2,3,5,7,11,13]
    assert actual == expected