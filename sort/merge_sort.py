import os 

"""
Explanation from GeekForGeeks :
Merge Sort is a Divide and Conquer algorithm. 
It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. 
The merge() function is used for merging two halves. 
The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. 

Best//Worst/Average-performance: O(n log n)
"""


def mergeSort(array):

    if len(array) > 1 :

        middle = len(array)//2

        L = array[:middle]
        R = array[middle:]

        mergeSort(L)
        mergeSort(R)

        #Merging part
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i+=1
            else:
                array[k] = R[j]
                j+=1
            k+=1

        #Check if any element left
        while i < len(L):
            array[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            array[k] = R[j]
            j+=1
            k+=1

if __name__ == '__main__':

    array = [4, 2, 17, 8, 1, 5, 7, 12, 21, 18]

    mergeSort(array)

    print(array)