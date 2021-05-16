import os 

"""
Bubble sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

Complexity :
- Worst and Average Case Time Complexity: O(n^2). Worst case occurs when array is reverse sorted.
- Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
"""

def bubbleSort(array):

    for i in range(len(array)):
        swapped = False 

        for j in range(len(array)-i-1):

            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if swapped == False:
            break
    return array

if __name__ == '__main__':

    array = [4, 2, 17, 8, 1, 5, 7, 12, 21, 18]

    sorted_array = bubbleSort(array)

    print(sorted_array)