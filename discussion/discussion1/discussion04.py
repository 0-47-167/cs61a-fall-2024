def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    cnt = 0
    for i in range(0,10,1):
        if(has_digit(n,i)):
            cnt += 1
    return cnt


def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    if(n == 0 & k == 0): return True
    while(n):
        x = n % 10
        if(x == k): return True
        n = n // 10
    return False

# print(has_digit(0, 0))
# print(unique_digits(13173131))