class Solution(object):
    # 94.66% + 9.32%
	def maxSubArray(self, nums):    
        maxsofar=max(nums)
        summ=0
        for i in list(range(len(nums))):
        	#accumulate the sum
            summ+=nums[i]
            if summ>=0:
            	#keep refreshing current max
            	#if it goes down(when encounter negative element, it won't refresh
                maxsofar=max(maxsofar, summ)
            else:
            	#otherwise, if all negative, re-initial the sum count, return max(ini_string) 
            	summ=0
        return maxsofar

    # second time - similar to method one, but use while-loop occupying fewer space
    # 36ms + 13.5MB (97.50% + 85.66%)
    def maxSubArray(self, nums: List[int]) -> int:
        # initialize
        summ,i = 0,0
        currentmax = max(nums)
        # single element list
        if len(nums) == 1:
            return nums[0]
        while i < len(nums):
            summ += nums[i]
            if summ < 0:
                summ = 0
            else:
                currentmax = max(currentmax,summ)
            i += 1
        return currentmax

    # 94.66% + 68.11%
    def maxSubArray2(self, nums): 
    	ret=float('-inf')
        # because the result would be the 1st element if it's descending list
        prevsum=nums[0] 
        
        for i in range(1,len(nums)):
            # exclude the first element
            prevsum=max(nums[i],nums[i]+prevsum) 
            # 这一步和method1的比较summ是否>1道理一样
            # 是为了看这一位数有没有把sum拉低到负数，如果没有，就不会重新开始计数
            # 为什么拉低到负数就要重新开始计数呢？--相当于让后一个数输在起跑线上，还不如让它从0开始
            
            ret=max(ret,prevsum) #refreshing sum for each iteration

        # return the 1st element of sum of some sub-array
        ret=max(nums[0],ret)
        
        return ret

    #similar to the first method's idea 57.02% + 98.49%
    def maxSubArray3(self, nums):
        local_max, global_max = 0, nums[0]
        for num in nums:
            global_max = max(global_max, local_max+num)
            local_max = max(0, local_max+num)
        return global_max