def solution(A):
    west_cars = 0
    cnt_passings = 0

    for idx in xrange(len(A)-1, -1, -1):
        if A[idx] == 0:
            cnt_passings += west_cars
            if cnt_passings > 1000000000:
                return -1
        else:
            west_cars += 1

    return cnt_passings
