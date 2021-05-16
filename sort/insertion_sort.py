import os 

"""
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. 
The array is virtually split into a sorted and an unsorted part. 
Values from the unsorted part are picked and placed at the correct position in the sorted part.

Complexity :
- Time complexity O(n^2) 
- Time complexity O(n) if array is already sorted
"""

def insertionSort(array):

    for i in range(1, len(array)):
        tmp = array[i]

        j = i - 1
        while j >= 0 and tmp < array[j]:
            array[j+1] = array[j]
            j-=1

        #j is always 1 step to far away on the left here
        array[j+1] = tmp

    return array

if __name__ == '__main__':

    array = [4, 2, 17, 8, 1, 5, 7, 12, 21, 18]

    sorted_array = insertionSort(array)

    print(sorted_array)
