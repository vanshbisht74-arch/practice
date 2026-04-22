arr = [2, 66, 30, 5, 9, 10]   # input array
n = len(arr)                  # size of array

def max_heap(arr, n, i):
    largest = i              # assume current index is largest

    left = 2*i + 1           # left child index
    right = 2*i + 2          # right child index

    # check if left child exists AND is greater than current largest
    if left < n and arr[largest] < arr[left]:
        largest = left       # update largest to left child

    # check if right child exists AND is greater than current largest
    if right < n and arr[largest] < arr[right]:
        largest = right      # update largest to right child

    # if largest is not the root (i), we need to swap
    if largest != i:
        # swap parent with largest child
        arr[i], arr[largest] = arr[largest], arr[i]

        # recursively heapify the affected subtree
        max_heap(arr, n, largest)


#Build Max Heap

# start from last non-leaf node and go backwards
# n//2 - 1 gives last parent node
for i in range(n//2 - 1, -1, -1):
    max_heap(arr, n, i)      # apply heapify on each node


# print final max heap
print("Max Heap:", arr)