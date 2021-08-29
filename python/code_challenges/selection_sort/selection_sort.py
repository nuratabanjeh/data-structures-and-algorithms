# Pseudocode
# SelectionSort(int[] arr)
#     DECLARE n <-- arr.Length;
#     FOR i = 0; i to n - 1  
#         DECLARE min <-- i;
#         FOR j = i + 1 to n
#             if (arr[j] < arr[min])
#                 min <-- j;

#         DECLARE temp <-- arr[min];
#         arr[min] <-- arr[i];
#         arr[i] <-- temp;



def selection_sort(arr):
    for i in range(1, len(arr)):
        j= i - 1
        temp = arr[i]

        while j >= 0 and temp < arr[j]:
            j = j-1

        arr.pop(i)
        arr.insert(j+1,temp)

    return arr


print(selection_sort([5,8,6,4,1]))
