import time

"""
Dynamic programming : Fibonacci series is a case of overlapping subproblems
"""
#Simple recursive approach
def simple_fib(n):
    if n<=1:
        return n  
    else:
        return simple_fib(n-1) + simple_fib(n-2)


#Memoization approach (Top Down), we store solutions to subproblems in a lookup table so that we can reuse them instead of recomputing them if needed
def mem_fib(n, lookup):

    if n == 0 or n == 1:
        lookup[n] = n
    
    if lookup[n] is None:
        lookup[n] = mem_fib(n-1, lookup) + mem_fib(n-2, lookup)

    return lookup[n]

#Tabulation approach (Bottom Up), starting from the beginning, we store the calculated values one by one in an array and we return the last result
def tab_fib(n):
  
    f = [0]*(n+1)
    f[1] = 1
  
    for i in range(2 , n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


if __name__ == '__main__':

    n = 30

    start = time.time() 
    print(simple_fib(n))
    end = time.time()
    print(f"Simple recursive approach for n = {n} took {(end - start):.10f} sec")

    lookup = [None] *101
    start = time.time() 
    print(mem_fib(n,lookup))
    end = time.time() 
    print(f"Memoization approach for n = {n} took {(end - start):.10f} sec")

    start = time.time() 
    print(tab_fib(n))
    end = time.time()
    print(f"Tabulation approach for n = {n} took {(end - start):.10f} sec")