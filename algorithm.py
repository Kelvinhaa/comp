# selection, quick, merge, bubble, insertion

def selection_sort(arr):
    for i in range(len(arr) - 1):
        cur_min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j
                
        arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]
       
    return arr

# print(selection_sort([1, 2, 9, 3, 4, 10]))


def quick_sort(arr, low, high):
    if low < high:
        partition_pos = partition(arr, low, high)
        quick_sort(arr, low, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, high)
    return arr
def partition(arr, low, high):
    i = low
    j = high - 1
    pivot = arr[high]
    while i < j:
        while i < high and arr[i] < pivot:
            i += 1
        while j > low and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
    return i

# arr = [2, 1, 8, 6, 5, 7, 3, 4]
# print(quick_sort(arr, 0, len(arr) - 1))

        


if __name__ == '__main__':
assert selection_sort([1, 2, 9, 3, 4, 5, 11, 10]) == [1, 2, 3, 4, 5, 9, 10, 11]  

