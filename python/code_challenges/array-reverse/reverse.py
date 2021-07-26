arr=[10,20,30,40]

def reverseArray(arr):
    
    a=0
    b=len(arr)-1
    while a<b:
       arr[a], arr[b] = arr[b], arr[a]
       a += 1
       b -= 1
    return arr

    

print(reverseArray(arr))