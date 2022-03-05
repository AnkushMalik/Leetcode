class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words)==1: return True
        
        def checkOrder(s1,s2):
            n = min(len(s1),len(s2))
            for i in range(n):
                p = order.index(s1[i])
                q = order.index(s2[i])
                if p<q: return True
                elif p>q: return False
            if s1[:n]==s2[:n]:
                return False if len(s1)>len(s2) else True
        
        for i in range(1,len(words)):
            if not checkOrder(words[i-1],words[i]):
                return False
        return True
            