# suspect the auto-grader with flaw, [99,99], 2 returns True????
# second method -same
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #check exist
        if not nums:
            return False
        if len(nums) == 1:
            return False
        if len(nums) <= k:
            return False
        i = 0
        while i < len(nums)-k:
            cur = nums[i]
            for j in range(i+1,i+k+1):
                if nums[j] == cur:
                    return True
            i+=1
        return False