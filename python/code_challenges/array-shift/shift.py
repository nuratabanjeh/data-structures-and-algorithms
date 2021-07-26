a=5
b=16
arr1=[2,4,6,-8]
arr2=[42,8,15,23,42]

def insertShiftArray(arr,a):
  if not( type(arr) == type([]) ):
    return 'error'
  newArr=[]
  if len(arr)%2==0:
    t=int(len(arr)/2)
  else:
    t=int(len(arr)/2)+1
  newArr = arr[0:t]+[a]
  newArr = newArr+arr[t:len(arr)]

  return newArr


print(insertShiftArray(arr2,b))
