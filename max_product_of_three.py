"""
https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
"""

# Aim to return the maximal product between:
#   - the contiguous pair at the beginning of the sequence with the last element and
#   - the contiguous triplets at the end of the sequence
#
# Assumptions/Requirements
#   - The array is non-empty
#   - The array has at least three elements
#
# Caveats
#   - The array has to be sorted first

"""
Optimal Solution using Python heapq class
```python

    def betterSolution(A):
        if len(A) < 3:
            raise Exception("Invalid input")

        minH = []
        maxH = []

        for val in A:
            if len(minH) < 2:
                heapq.heappush(minH, -val)
            else:
                heapq.heappushpop(minH, -val)

            if len(maxH) < 3:
                heapq.heappush(maxH, val)
            else:
                heapq.heappushpop(maxH, val)


        max_val = heapq.heappop(maxH) * heapq.heappop(maxH)
        top_ele = heapq.heappop(maxH)
        max_val *= top_ele
        min_val = -heapq.heappop(minH) * -heapq.heappop(minH) * top_ele

        return max(max_val, min_val)
```
"""

class Empty(Exception):
    pass


def solution(A):
    if len(A) == 0:
        raise Empty("The sequence is empty")
    A.sort()
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])


print(solution([-3,1,2,-2,5,6]))
