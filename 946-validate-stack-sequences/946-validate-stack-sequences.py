class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        temp = []
        for i in pushed:
            temp.append(i)
            while temp and temp[-1]==popped[0]:
                temp.pop()
                popped.pop(0)
            if not temp and not popped: return True
        return False