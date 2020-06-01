"""
https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
"""
# def solution(A, B, K):
#     _range = None
#     count = 0
#     if not A % K:
#         _range = range(A, B + 1, K)
#     else:
#         _range = range(A + (K - A % K), B + 1, K)

#     for i in _range:
#         count += 1

#     return count


def solution(A, B, K):
    min_value =  ((A + K - 1) // K) * K

    if min_value > B:
      return 0

    return ((B - min_value) // K) + 1
