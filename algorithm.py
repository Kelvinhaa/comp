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

if __name__ == '__main__':
    assert selection_sort([1, 2, 9, 3, 4, 5, 11, 10]) == [1, 2, 3, 4, 5, 9, 10, 11]  