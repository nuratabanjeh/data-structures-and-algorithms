def BinarySearch(arr, target):
  if not( type(arr) == type([]) ):
    return 'error'

  high = len(arr) - 1
  low = 0

  while low <= high:
    mid = low + (high - low) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

print(BinarySearch([-2,-1,4, 8, 15, 16, 23, 42,50,72,100,105,113], 105))
