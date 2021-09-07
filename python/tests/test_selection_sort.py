# from code_challenges.selection_sort.selection_sort import selection_sort

def selection_sort(arr):
    for i in range(1, len(arr)):
        j= i - 1
        temp = arr[i]

        while j >= 0 and temp < arr[j]:
            j = j-1

        arr.pop(i)
        arr.insert(j+1,temp)

    return arr


    ###########test#######

def test_sort():
    actual = selection_sort([6,5,3,4,1])
    expected = [1,3,4,5,6]
    assert actual == expected

    
def test_reverse_sorted():    
    actual= selection_sort([20,18,12,8,5,-2])
    expected = [-2,5,8,12,18,20]
    assert actual == expected


def test_few_uniques():    
    actual= selection_sort([5,12,7,5,5,7])
    expected = [5,5,5,7,7,12]
    assert actual == expected

def test_nearly_sorted():    
    actual= selection_sort([2,3,5,7,13,11])
    expected = [2,3,5,7,11,13]
    assert actual == expected



