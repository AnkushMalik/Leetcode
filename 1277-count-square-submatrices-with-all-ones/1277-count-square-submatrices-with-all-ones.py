class Solution:
    def countSquares(self, M: List[List[int]]) -> int:
        ans, m, n = 0, len(M), len(M[0])
        from itertools import product
        for i, j in product(range(m), range(n)):
            if i > 0 and j > 0:
                if M[i - 1][j] and M[i][j - 1] and M[i - 1][j - 1] and M[i][j]:
                    M[i][j] += min(M[i - 1][j], M[i][j - 1], M[i - 1][j - 1])
            ans += M[i][j]
        print(M)
        return ans