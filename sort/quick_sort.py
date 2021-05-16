import os

"""
Explanation from GeekForGeeks :
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. 
There are many different versions of quickSort that pick pivot in different ways. 

    Always pick first element as pivot.
    Always pick last element as pivot (implemented below)
    Pick a random element as pivot.
    Pick median as pivot.

The key process in quickSort is partition(). 
Target of partitions is, given an array and an element x of array as pivot,
put x at its correct position in sorted array and put all smaller elements (smaller than x) before x,
and put all greater elements (greater than x) after x. All this should be done in linear time. 

Average-performance: O(n log n)
Worst-case performance: O(n^2)
"""

#We take the last element as pivot
def partition(array, low, high):

    i = (low - 1) #index of smaller element
    pivot = array[high]
    

    for j in range(low, high):

        if array[j] <= pivot :
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)


def quickSort(array, low, high):

    if low < high :
    
        p = partition(array, low, high)

        quickSort(array, low, p-1)
        quickSort(array, p+1, high)

    return array


if __name__ == '__main__':

    array = [4, 2, 17, 8, 1, 5, 7, 12, 21, 18]

    sorted_array = quickSort(array, 0, len(array)-1 )

    #print(sorted_array)
    print(sorted_array)