from typing import List


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        curr = self.head

        for _ in range(index):
            curr = curr.next

        return curr.val

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.length += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)

        if self.head is None:
            self.head = node
        else:
            curr = self.head

            while curr.next:
                curr = curr.next

            curr.next = node

        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return True

        curr = self.head

        for _ in range(index - 1):
            curr = curr.next

        curr.next = curr.next.next
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.head

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values