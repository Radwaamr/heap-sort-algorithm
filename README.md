# Heap Sort Algorithm

## a. Algorithm to Perform Heap Sort

### Step-by-Step Algorithm

Heap Sort is a comparison-based sorting technique that builds a binary heap from the input array and sorts the elements by repeatedly extracting the maximum value from the heap. The heap ensures efficient management of the largest (or smallest) elements during sorting.

#### Algorithm Steps:

**Build a Max Heap**:
Convert the input array into a Max Heap, where the largest element is always at the root.

**Extract the Maximum Element**:
Swap the root (largest value) with the last element in the heap.
Reduce the size of the heap by 1 and restore the Max Heap property for the remaining elements using the Heapify operation.

**Repeat**:
Continue swapping and heapifying until all elements are sorted in the array.

**Properties of a Max Heap**
A Max Heap is a complete binary tree where the value of the parent node is always greater than or equal to its child nodes.
The largest element is always stored at the root of the heap.

---

### Pseudo-code for Heap Sort

```plaintext

HeapSort(arr):
    Input: arr[]  // Array to be sorted
    Output: arr[] // Sorted array in ascending order

    1. Build a max heap from the input array:
        for i = (n // 2) - 1 to 0:  // Start from the last non-leaf node
            Heapify(arr, n, i)      // Ensure max heap property for each subtree

    2. Extract elements from the heap one by one:
        for i = n - 1 to 1:
            Swap(arr[0], arr[i])    // Move current root to the sorted position
            Heapify(arr, i, 0)      // Restore max heap property for the reduced heap

    3. Return arr[] as the sorted array

``` 
### Pseudo-code for the Heapify Subroutine

```plaintext

Heapify(arr, n, i):
    Input: arr[], n = size of the heap, i = index of the root node
    Output: None // Ensures max heap property for the subtree rooted at index i

    1. largest = i                // Assume the root is the largest
       left = 2 * i + 1           // Index of the left child
       right = 2 * i + 2          // Index of the right child

    2. If left < n and arr[left] > arr[largest]: // Check left child
        largest = left           // Update largest to left child

    3. If right < n and arr[right] > arr[largest]: // Check right child
        largest = right          // Update largest to right child

    4. If largest != i:          // If root is not the largest
        Swap(arr[i], arr[largest]) // Swap root with the largest child
        Heapify(arr, n, largest) // Recursively heapify the affected subtree
```

## b. Detailed Analysis of the Algorithm
### Time Complexity Analysis

#### Building the Max Heap:
Constructing a Max Heap takes O(n) time because the cost of heapifying decreases as you move down the tree levels.

#### Extracting Elements:
Extracting the root and heapifying the remaining heap for each element takes O(log n) per element. For n elements, this step takes O(n log n).

### Overall Time Complexity:
The total time complexity is:
\[
𝑂(𝑛log𝑛)
\]

This includes the time to build the Max Heap and the time to extract and heapify elements.
