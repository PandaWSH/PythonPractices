class Solution(object):
	def maxSubArray(self, nums):    
        maxsofar=max(nums)
        summ=0
        for i in list(range(len(n))):
        	#accumulate the sum
            summ+=nums[i]
            if summ>=0:
            	#keep refreshing current max
            	#if it goes down(when encounter negative element, it won't refresh
                maxsofar=max(maxsofar, summ)
            else:
            	#otherwise, if all negative, return max(ini_string) 
            	summ=0
        return maxsofar

    def maxSubArray2(self, nums): 
    	ret=-9999
        prevsum=nums[0]
        
        for i in range(1,len(nums)):
            prevsum=max(nums[i],nums[i]+prevsum)
            ret=max(ret,prevsum)

        ret=max(nums[0],ret)
        
        return ret
