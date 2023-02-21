class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        m = len(image)
        n = len(image[0])
        original_color = image[sr][sc]
        
        if original_color == color:
            return image
        
        print("sr ", sr, " sc ", sc, " col ", original_color, " new col ", color)
            
        # change the current pixel
        image[sr][sc] = color
            
        # check for 4 neighbors
        # sr sc-1
        # sr-1 sc
        # sr+1 sc
        # sr sc+1 
        if sc>0 and image[sr][sc-1] == original_color:
            image =  self.floodFill(image, sr, sc-1, color)
        if sr>0 and image[sr-1][sc] == original_color:
            image =  self.floodFill(image, sr-1, sc, color)
        if sr<m-1 and image[sr+1][sc] == original_color:
            image =  self.floodFill(image, sr+1, sc, color)
        if sc<n-1 and image[sr][sc+1] == original_color:
            image = self.floodFill(image, sr, sc+1, color)
        
            
        return image  
        
        
        
sol = Solution()
# print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))
print(sol.floodFill([[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0))