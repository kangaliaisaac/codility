"""
https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
"""


def solution(N, A):
    counters = [0] * N
    max_counter = 0
    for elem in A:
        if 1 <= elem <= N:
            counters[elem - 1] += 1
            if counters[elem - 1] > max_counter:
                max_counter = counters[elem - 1]
        else:
            counters = [max_counter] * N

    return counters
