# Merge Sort

merge sort is an algorithm that will split the array each time into half and re merge it together sorted from the smallest value to the biggest value.

# Pseudocode

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

# Trace

![img](sort1.jpg)

![img](sort2.jpg)

![img](sort3.jpg)

![img](sort4.jpg)

![img](sort5.jpg)

![img](sort6.jpg)

![img](sort7.jpg)

![img](sort8.jpg)

![img](sort9.jpg)

![img](sort10.jpg)

# Efficency:

Time: O(nlog(n))

Space: O(n)

