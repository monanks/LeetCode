class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        l = len(image)
        w = len(image[0])
        visited = []
        emp = [0]*w
        for i in range(l):
            visited.append(emp[:])
        
        def fill(r,c):
            oldColor = image[r][c]
            visited[r][c] = 1
            image[r][c] = newColor
            if r+1 < l and image[r+1][c] == oldColor and visited[r+1][c] == 0:
                fill(r+1,c)
            if r-1 >= 0 and image[r-1][c] == oldColor and visited[r-1][c] == 0:
                fill(r-1,c)
            if c+1 < w and image[r][c+1] == oldColor and visited[r][c+1] == 0:
                fill(r,c+1)
            if c-1 >= 0 and image[r][c-1] == oldColor and visited[r][c-1] == 0:
                fill(r,c-1)
        
        fill(sr,sc)
        return image

s = Solution()
print(s.floodFill([[0,0,0],[0,1,1]],1,1,1))