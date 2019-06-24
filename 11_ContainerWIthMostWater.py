class Solution:
    # my method
    def maxArea(self, height: List[int]) -> int:
        start, maxArea = 0, 0 
        end = len(height) - 1
        
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            maxArea = max(maxArea, area)
            
            if (height[start] < height[end]):
                start +=1
            else:
                end -=1
                
        return maxArea