"""
https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
"""

"""
Solution 1
----------

Runs in O(N lg N)
Note:
    Not optimal for chaotic or very large input

```python
    from collections import Counter


    def positive_int_arr(arr):
        for ind, elem in enumerate(arr):
            if elem > 0:
                return arr[ind:]


    def solution(A):
        if not A:
            return 1
        else:
            if all(elem < 1 for elem in A):
                return 1
            A.sort()
            B = positive_int_arr(A)
            _b = Counter(B)
            vals = [i for i in range(1, B[-1] + 1) if i not in _b.keys()]
            if vals:
                return vals[0]
            else:
                return B[-1] + 1
```
"""


"""
Solution 2
----------

Runs in O(m + n)
"""

def solution(A):
    seen = [False] * len(A)
    for value in A:
        if 0 < value <= len(A):
            seen[value - 1] = True

    for idx in range(len(seen)):
        if seen[idx] == False:
            return idx + 1

    return len(A) + 1


print(solution([1, 3, 6, 4, 1, 2]))
