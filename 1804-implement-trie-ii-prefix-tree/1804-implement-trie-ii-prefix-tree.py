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
        dic['$']=None

    def countWordsEqualTo(self, word: str) -> int:
        dic = self.dic
        for i in word:
            if i not in dic:
                return 0
            else:
                dic = dic[i]
        curr = dic["count"]
        children = 0
        for i in dic:
            if i!='$' and i!="count":
                children+=dic[i]["count"]
        return curr-children

    def countWordsStartingWith(self, prefix: str) -> int:
        dic = self.dic
        for i in prefix:
            if i not in dic:
                return 0
            else:
                dic = dic[i]
        return dic["count"]

    def erase(self, word: str) -> None:
        dic = self.dic
        for i in word:
            dic[i]["count"]-=1
            dic = dic[i]