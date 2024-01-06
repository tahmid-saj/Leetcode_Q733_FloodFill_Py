class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image, x, y, oldColor, newColor):
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]): return
            if image[x][y] != oldColor: return
            if image[x][y] == oldColor: image[x][y] = newColor

            dfs(image, x - 1, y, oldColor, newColor)
            dfs(image, x + 1, y, oldColor, newColor)
            dfs(image, x, y - 1, oldColor, newColor)
            dfs(image, x, y + 1, oldColor, newColor)

        if image[sr][sc] != color: dfs(image, sr, sc, image[sr][sc], color)
        else: return image
        
        return image
