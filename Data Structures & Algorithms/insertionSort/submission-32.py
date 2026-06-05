from typing import List
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        arr = []
        for i in range(0, len(pairs)):
            current = pairs[i]
            j = i - 1
            while j >= 0 and pairs[j].key > current.key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j + 1] = current
            new_pair=[]
            for k in range(0, len(pairs)):
                new_pair.append(pairs[k])
            arr.append(new_pair)
        return arr