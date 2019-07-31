class Solution:
	# slow (44ms + 13.2MB)(20.49%+41.84%)
    def rob(self, nums: List[int]) -> int:
        rob, not_rob = 0, 0
        for num in nums:
            rob = not_rob + num
            not_rob = max(rob, not_rob)
        return max(rob, not_rob)

# second time
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        elif n == 1:
            return nums[0]

        robValues = [0]*n
        
        robValues[0] = nums[0]       # doing our best here, robbing the only house
        robValues[1] = max(nums[:2]) # have the option to rob either house
        
        for i in range(2, n):
			# best total rob value is either robbing house i along with the previous best total 
			# or just not rob house i at all and take whatever up to the adjacent house to the left
            robValues[i] = max(nums[i]+robValues[i-2], robValues[i-1])
                    
        return robValues[n-1]

    # 36ms + 13.3 MB
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        i = 3
        dp = [nums[0]] + [nums[1]] + [nums[0] + nums[2]] + [0] * (n-3)
        while i < n:
            dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i])
            i += 1
        return max(dp)

