# Homework 3 


## Question 1

Proposition: By slightly modifying the kth smallest element algorithm to use the abs(median,A[i]) instead of A[i] we 
can create an ϴ(N) algorithm to find the K closest elements to the median.

1.  Find the median by value by using the kth smallest algorithm with k = floor((n+1)/2).
   Let m = findKthSmallest(A, floor((n+1)/2))
   - This takes ϴ(n) time
2. Create array B of size N where each index contains the (abs(A[i]-m),A[i]) for 1 <= i <= n
  ```text
    A = [0,30,2,6,14,62]
    M = kthSmallest(A, 3) # M = 6
    # After partition A = [2,0,6,62,14,30] as example. 
    # Guaranteed that all elements left of M are <= M and all elements right of M >= M
    B = [(4,2),(6,0),(0,6),(56,62),(8,14),(24,30)]
```
   - This takes ϴ(n) time
3. Run modified kth smallest algorithm with input K on B only using B[i][0] as the value for partitioning. 
   - Now array B will contain elements [i,i+1,i+2..k] where k elements are the closest to the median
   ```text
   B = [(4,2),(6,0),(0,6),(56,62),(8,14),(24,30)]
   K = 4
   S = kthSmallestModified(B, K)
   # After partitioning from KthSmallestModified B = [(4,2),(6,0),(0,6),(8,14),(56,62),(24,30)] as example
   # Guaranteed that all elements left of S have abs(A[i]-M) <= S and all elements right of S have abs(A[i]-M) >=S
```
    - This takes ϴ(n) time
4. Create a result array C of size K where each index contains B[i][0] for  1 <= i <= k. This will contain 
   the elements with the K closest values to the median
   ```text
   B = [(4,2),(6,0),(0,6),(8,14),(56,62),(24,30)]
   C = [K]
   for i = 1 to K:
      C[i] = B[i][1]
   # C = [2,0,6,14]
   ```
    - This takes ϴ(k) time
5. Return array C

Time Complexity: ϴ(n) + ϴ(n) + ϴ(n) + ϴ(k) = ϴ(n)


## Question 2

- We know by n//k how many groups we have 
- Then just iterate restricting the size of the heap to k elements


## Question 4




```python

       
   
   
def lis(S):
    n = len(S)
    dp_arr = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if S[i] < S[j]:
                dp_arr[i] = max(dp_arr[i], 1 + dp_arr[j])
    return max(dp_arr)
  
```


## Question 5

- https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm
- 
