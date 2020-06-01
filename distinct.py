"""
https://app.codility.com/programmers/lessons/6-sorting/distinct/
"""

from collections import Counter


def solution(A):
    return 0 if len(A) == 0 else len(Counter(a))
