"""
https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

Proof: https://github.com/daotranminh/playground/blob/master/src/codibility/MinAvgTwoSlice/proof.pdf
"""

def solution(A):
    L = len(A)
    min_index = 0
    min_value = 10001
    for idx in range(L - 1):
        if (A[idx] + A[idx + 1]) / 2.0 < min_value:
            min_index = idx
            min_value = (A[idx] + A[idx + 1]) / 2.0
        if idx < L - 2 and (A[idx] + A[idx + 1] + A[idx + 2]) / 3.0 < min_value:
            min_index = idx
            min_value = (A[idx] + A[idx + 1] + A[idx + 2]) / 3.0

    return min_index



print(solution([4,2,2,5,1,5,8]))
