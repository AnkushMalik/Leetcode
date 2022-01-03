class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color==newColor: return image
        def doFloodFill(image, sr, sc):
            image[sr][sc]=newColor
            if sr>0 and image[sr-1][sc]==color:
                doFloodFill(image, sr-1, sc)
            if sr<len(image)-1 and image[sr+1][sc]==color:
                doFloodFill(image, sr+1, sc)
            if sc>0 and image[sr][sc-1]==color:
                doFloodFill(image, sr, sc-1)
            if sc<len(image[0])-1 and image[sr][sc+1]==color:
                doFloodFill(image, sr, sc+1)
        doFloodFill(image,sr,sc)
        return image