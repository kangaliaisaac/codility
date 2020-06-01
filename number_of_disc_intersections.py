"""https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/

Elaborate explanation can be found here:

http://www.lucainvernizzi.net/blog/2014/11/21/codility-beta-challenge-number-of-disc-intersections/
"""

def solution(A):
    # Collect, on the number line, all touch points for every radius
    # (sequence elements) from the given points of origin (sequence indices)
    touch_points = []

    for ind, elem in enumerate(A):
        # '-1' indicates the left touch point
        # '+1' indicates the right touch point
        touch_points += [(ind - elem, +1), (ind + elem, -1)]

    touch_points.sort(key=lambda x: (x[0], -x[1]))
    intersections, active_circles = 0, 0

    for _, circle_count_delta in touch_points:
        intersections += active_circles * (circle_count_delta > 0)
        active_circles += circle_count_delta

        # Return -1 if the number of intersecting pairs exceeds 10E6
        if intersections > 10E6:
            return -1

    return intersections


print(solution([1, 5, 2, 1, 4, 0]))
