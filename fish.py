"""https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/"""


class Empty(Exception):
    pass


class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def peek(self):
        if self.is_empty():
            raise Empty("The stack is empty!")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("The stack is empty!")
        return self._data.pop()

    def push(self, e):
        self._data.append(e)


def solution(A, B):
    survived = 0
    S = ArrayStack()

    for ind in range(len(A)):
        if B[ind] == 0:
            while not S.is_empty():
                if S.peek() > A[ind]:
                    break
                else:
                    S.pop()
            else:
                survived += 1
        else:
            S.push(A[ind])

    survived += len(S)

    return survived

print(solution([4,3,2,1,5], [0,1,0,0,0]))
