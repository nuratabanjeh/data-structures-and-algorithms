def mergesort(arr):
    n = len(arr)
    if n >1:
        mid = int(n/2)
        left = arr[0:mid]
        right = arr[mid:n]
        mergesort(left)
        mergesort(right)
        merge(left, right, arr)
    return arr

def merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i= i + 1
        else:
            arr[k] = right[j]
            j= j +1
        k = k+1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


##########TESTS######

def test_mergesort():
    actual = mergesort([6,5,3,4,1])
    expected = [1,3,4,5,6]
    assert actual == expected

    
def test_reverse_sorted():    
    actual= mergesort([20,18,12,8,5,-2])
    expected = [-2,5,8,12,18,20]
    assert actual == expected


def test_few_uniques():    
    actual= mergesort([5,12,7,5,5,7])
    expected = [5,5,5,7,7,12]
    assert actual == expected

def test_nearly_sorted():    
    actual= mergesort([2,3,5,7,13,11])
    expected = [2,3,5,7,11,13]
    assert actual == expected
