from typing import List

class LinkedList:

    def __init__(self):
        self.length = 0
        self.arr = []

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        return self.arr[index]

    def insertHead(self, val: int) -> None:
        self.arr.insert(0, val)
        self.length += 1

    def insertTail(self, val: int) -> None:
        self.arr.append(val)
        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False

        del self.arr[index]
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        return self.arr