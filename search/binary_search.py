import os


def recursive_binary_search(array,start,end,value):

    if end >= start:

        middle = (start + end)//2

        if array[middle] == value:
            return middle
        elif array[middle] > value:
            return recursive_binary_search(array,start,middle-1,value)
        else:
            return recursive_binary_search(array,middle+1,end,value)

    else:
        return -1



def iterative_binary_search(array, value):
    n = len(array)
    low = 0
    high = n - 1
    mid = 0

    while low <= high:
        mid = (high + low)//2
        if array[mid] > value:
            high = mid - 1
        elif array[mid] < value:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':

    array = [1,2,4,5,6,6,7,9,12,13,14,15,15,15,16,18,21,22,24,26,27,29,30,32]

    print("##### RECURSIVE BINARY SEARCH #####")

    no_result_recursive = recursive_binary_search(array,0,len(array)-1,10)

    if no_result_recursive == -1:
        print("Test no element : OK")
    else:
        print("Test no element : element found at index ",str(no_result_recursive))

    result_recursive = recursive_binary_search(array,0,len(array)-1,14)

    if result_recursive == -1:
        print("Test element present : No element found")
    else:
        print("Test element present : element found at index ",str(result_recursive))

    print("##### ITERATIVE BINARY SEARCH #####")

    no_result_iterative = iterative_binary_search(array,10)

    if no_result_iterative == -1:
        print("Test no element : OK")
    else:
        print("Test no element : element found at index ",str(no_result_iterative))

    result_iterative = iterative_binary_search(array,14)

    if result_iterative == -1:
        print("Test element present : No element found")
    else:
        print("Test element present : element found at index ",str(result_iterative))