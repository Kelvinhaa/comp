# selection, quick, merge, bubble, insertion
def insertion(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

print(insertion([1, 5, 2, 4]))     




def selection_sort(arr):
    for j in range(len(arr) - 1)-1:
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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    # Step 1: Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Step 2: Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Step 3: Compare and merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Step 4: Add any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

        


# if __name__ == '__main__':
#     assert selection_sort([1, 2, 9, 3, 4, 5, 11, 10]) == [1, 2, 3, 4, 5, 9, 10, 11]  
from collections import deque
def bfs(graph, startNode):
    visited = set()
    queue = deque([startNode])
    order = []

    while queue:
        curNode = queue.popleft()
        if curNode not in visited:
            visited.add(curNode)
            order.append(curNode)
            queue.extend(graph[curNode])
    return order

graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
print(bfs(graph, 'A'))

# dfs using stack
def dfs_stack(graph, startNode):
    visited = set()
    stack = [startNode]
    while stack:
        curNode = stack.pop()
        if curNode not in visited:
            print(curNode)
            visited.add(curNode)
            stack.extend(reversed(graph[curNode]))

# dfs using recursion
VISITED = set()
def dfs_recur(graph, startNode):
    if not graph:
        return 
    if startNode not in VISITED:
        print(startNode)
        VISITED.add(startNode)
        for neighor in graph[startNode]:
            dfs_recur(graph, neighor)

# dfs_recur(graph, 'A')