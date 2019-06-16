class Solution:
	#my method, use set() to remove duplicate, then compare length
	# 40ms + 19MB (93.52% + 41.86%)
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False    
        numss = set(nums)
        if len(nums) != len(numss):
            return True 
        return False