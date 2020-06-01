"""https://app.codility.com/programmers/lessons/6-sorting/triangle/"""


"""
Description
-----------

For a non-empty sequence A with N elements such that 0 <= P < Q < R < N,
return 1 if the following conditions are satisfied:
    - A[P] + A[Q] > A[R]
    - A[P] + A[R] > A[Q]
    - A[Q] + A[R] > A[P]

Hint
----

    - If the first condition is satisfied, then the other two conditions will
        be satisfied by default

Caveats
-------

    - Sequence should not be empty; should have at least three elements

Pre-requisites
--------------

The sequence A has to be sorted in ascending order first

Runs in
    - O(N log N) in best/average case because it will return immediately it
        finds the earliest match
    - O(N - 2) if it has to go through the entire sequence
"""

def solution(A):
    if len(A) >= 3:
        A.sort()
        for idx in range(len(A) - 2):
            if A[idx] + A[idx + 1] > A[idx + 2]:
                return 1

    return 0
