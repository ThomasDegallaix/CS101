import os


"""
Heap-sort with Max heap :
1. Build a max heap from the input data. 
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1.
   Finally, heapify the root of the tree. 
3. Repeat step 2 while the size of the heap is greater than 1.

Time complexity of heapify is O(Logn). Time complexity of createAndBuildHeap() is O(n) and the overall time complexity of Heap Sort is O(nLogn).

A heap is a complete binary tree : Each level is completely filled except possibly the last. All nodes are as left as possible.
"""


def heapify(arr,n,i):
    left_child = 2*i+1
    right_child = 2*i+2

    #init
    largest = i

    # See if left child of root exists and is greater than root
    # We use the condition l or r < n because we use a complete binary tree, each level is complete with all nodes as left as possible
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    #If swap needed
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]

        heapify(arr,n,largest)

def heapSort(arr):

    n = len(arr)

    #Build maxheap
    for i in range (n//2-1,-1,-1):
        heapify(arr,n,i)

    #We extract elements one by one
    for j in range(n-1,0,-1):
        arr[0], arr[j] = arr[j], arr[0]
        #j = n - 1 so we extract the last value that has been swapped (which is the largest) from the heapify procedure
        #After swapping we need to rebuild the max heap shape via heapify
        heapify(arr,j,0)

if __name__  == '__main__':

    arr = [12, 11, 13, 5, 6, 7]

    heapSort(arr)

    print(arr)