class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = len(heights)
        ori = heights.copy()
        
        for i in range(len(heights) - 1):
            for j in range(len(heights) - 1 - i):
                if heights[j] > heights[j+1]:
                    temp = heights[j]
                    heights[j] = heights[j+1]
                    heights[j+1] = temp
                    
        for i in range(len(ori)):
            if heights[i] == ori[i]:
                count = count - 1
                
        return count