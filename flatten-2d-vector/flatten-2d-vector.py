class Vector2D:

    def __init__(self, vec: List[List[int]]):
        arr = []
        for el in vec:
            for i in el:
                arr.append(i)
        self.vec = arr
        self.ptr = 0

    def next(self) -> int:
        self.ptr+=1
        return self.vec[self.ptr-1]
        
    def hasNext(self) -> bool:
        return True if self.ptr<len(self.vec) else False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()