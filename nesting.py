"""https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/"""

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


def solution(S):
    _S = ArrayStack()
    for symbol in S:
        if symbol == "(":
            _S.push(symbol)
        elif symbol == ")":
            if _S.is_empty():
                return 0
            if "(" != _S.pop():
                return 0

    return 1 if _S.is_empty() else 0


print(solution("(()(())())"))
print(solution("())"))
