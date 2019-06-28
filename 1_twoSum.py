class Solution:
	# my method 1
	# 912ms [O(n^2)] + 13.7[O(1)] MB(29.62% + 87.15%)
	def twoSum(self, nums, target):
        for i in range(len(nums)):
            try:
                ind = nums[i+1::].index(target - nums[i])
                return[i,i+ind+1]
            except:
                pass

    # my method 2: hashtable one pass solution
    # 40ms [O(n)]+ 14.6 MB[O(n)] (80.21% + 21.03%)
    def twoSum(self, nums, target):
        diction = {}
        for i,e in enumerate(nums):
            if e not in diction:
                diction[target - e] = i
            else:
                return[diction[e],i]

