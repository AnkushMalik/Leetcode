'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 
'''

class Solution:
    winData = {}
    def findWinner(self, n):
        if n==1: return 0
        else:
            if n in self.winData: return self.winData[n]
            for i in range(1,int(n**0.5)+1):
                if n%i==0:
                    if n-i not in self.winData:
                        self.winData[n-i] = self.findWinner(n-i)
                    if not self.winData[n-i]: return 1
            return 0
    def divisorGame(self, n: int) -> bool:
        return self.findWinner(n)
