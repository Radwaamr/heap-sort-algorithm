def heapify(A, n, i):
    largest = i
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than the root
    if left < n and A[left] > A[largest]:
        largest = left

    # Check if right child exists and is greater than the current largest
    if right < n and A[right] > A[largest]:
        largest = right

    # If the largest is not the root
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # Swap
        heapify(A, n, largest)  # Recursively heapify the affected subtree

def heapSort(A):
    n = len(A)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]  # Swap the root with the last element
        heapify(A, i, 0)  # Restore the heap property for the reduced heap

    return A

# Example usage
arr = [4, 10, 3, 5, 1]
print("Original array:", arr)
sorted_array = heapSort(arr)
print("Sorted array:", sorted_array)
