class DynamicArray:
    def __init__(self, capacity: int):
        self.c = capacity
        self.n = 0
        self.a = [0] * capacity

    def get(self, i): return self.a[i]
    def set(self, i, v): self.a[i] = v

    def pushback(self, v):
        if self.n == self.c:
            self.c *= 2
            self.a = self.a + [0] * (self.c // 2)
        self.a[self.n] = v
        self.n += 1

    def popback(self):
        self.n -= 1
        return self.a[self.n]

    def getSize(self): return self.n
    def getCapacity(self): return self.c