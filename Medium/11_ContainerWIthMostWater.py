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

    # second time - same
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        curmax = 0
        
        while left < right:
            width = right - left
            cur = width * min(height[left],height[right])
            curmax  = max(cur,curmax)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
                
        return curmax