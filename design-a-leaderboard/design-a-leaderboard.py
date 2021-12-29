class Leaderboard:

    def __init__(self):
        self.scoreboard = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scoreboard:
            self.scoreboard[playerId]+=score
        else:
            self.scoreboard[playerId]=score

    def top(self, K: int) -> int:
        scores = list(self.scoreboard.values())
        scores.sort(reverse = True)
        return sum(scores[:K])
        
        

    def reset(self, playerId: int) -> None:
        self.scoreboard[playerId]=0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)