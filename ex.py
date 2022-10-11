def is_palindrome(s, t):
    n = len(s)
    retval = True
    for i in range(n):
        if s[i] != t[n - i - 1]:
            retval = False
        else:
            retval = True
    n = len(t)
    for i in range(t):
        if t[i] != s[n - i - 1]:
            retval = False
        else:
            retval = True

    return retval


def lis(S):
    n = len(S)
    dp_arr = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if S[i] < S[j]:
                dp_arr[i] = max(dp_arr[i], 1 + dp_arr[j])
    return max(dp_arr)



S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def lis_recur(i,j):
    if i < 0:
        return 0
    if S[i] > S[j]:
        return lis_recur(i-1,j)
    # elif S[i] <= S[j]:
    return max(lis_recur(i-1,j), 1 + lis_recur(i-1,i))


def find_elements_near_median(A):
    # find median of A
    n = len(A)


