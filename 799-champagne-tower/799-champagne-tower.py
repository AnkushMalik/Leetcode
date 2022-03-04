class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0]*i for i in range(1,102)]
        tower[0][0] = poured
        for i in range(query_row+1):
            for j in range(i+1):
                excessOneSide = (tower[i][j]-1)/2
                if excessOneSide>0:
                    tower[i+1][j]+=excessOneSide
                    tower[i+1][j+1]+=excessOneSide
        return min(1,tower[query_row][query_glass])
        