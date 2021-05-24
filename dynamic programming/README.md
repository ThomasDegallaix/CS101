Dynamic Programming (DP) is an algorithmic technique for solving an optimization problem by breaking it down into simpler subproblems and utilizing the fact that the optimal solution to the overall problem depends upon the optimal solution to its subproblems.

What are the characteristics of a problem that tells us that we can apply DP to solve it:

1. Overlapping Subproblems 
    Subproblems are smaller versions of the original problem. Any problem has overlapping sub-problems if finding its solution involves solving the same subproblem multiple times.
    Ex: Fibonacci => for fib(5) we need fib(4) and fib(3), for fib(4) we need fib(2) and ALSO fib(3)
  
2. Optimal Substructure Property 
    Any problem has optimal substructure property if its overall optimal solution can be constructed from the optimal solutions of its subproblems.
    Ex: Shortest path => Optimal paths from A to B and from B to C give optimal path from A to C


Def from GeekforGeeks :
Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later. This simple optimization reduces time complexities from exponential to polynomial. For example, if we write simple recursive solution for Fibonacci Numbers, we get exponential time complexity and if we optimize it by storing solutions of subproblems, time co

2 approaches : 
- Tabulation: Bottom Up
    In tabulated version, starting from the first entry, all entries are filled one by one.
- Memoization: Top Down
    Unlike the tabulated version, all entries of the lookup table are not necessarily filled in Memoized version. The table is filled on demand.