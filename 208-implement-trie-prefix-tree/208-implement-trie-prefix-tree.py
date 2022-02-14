class Trie:

    def __init__(self):
        self.dic = {}    

    def insert(self, word: str) -> None:
        dic = self.dic
        for i in word:
            if i in dic:
                dic[i]["count"]+=1
            else:
                dic[i] = {"count":1}
            dic = dic[i]
        dic['$'] = None
        

    def search(self, word: str) -> bool:
        dic = self.dic
        for i in word:
            if i in dic:
                dic = dic[i]
            else:
                return False
        return True if '$' in dic else False

    def startsWith(self, prefix: str) -> bool:
        dic = self.dic
        for i in prefix:
            if i in dic:
                dic = dic[i]
            else:
                return False
        return True