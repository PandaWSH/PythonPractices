class Solution:
	'''
	The math and algorithm behind this problem is actually fibonacci number
	0,1,2,3,5,8,13,21...
	'''

	# time exceed 
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

    # my method based on fibonacci number [81.72% + 65.74%]
    def climbStairs(self, n: int) -> int:        
        result = [1,1]
        for i in list(range(2,n+1)):
            stair = result[i-2] + result[i-1]
            result.append(stair)      
        return result[n]

    # my method similarly, but try to reduce space [90.09% + 57.87%]
    def climbStairs(self,n):
    	result = [1,1]
        for i in list(range(2,n+1)):
            stair = result[0] + result[1]
            result.append(stair)    
            result.pop(0) #delet the first one, maintain result as two elements list
        return result[1]

    # dynamic programming shared by others [98.61% + 24%]
    def climbStairs(self,n):
    	# creat a n-element list, each with 1 (because the first two were 1)
    	dp=[1]*n
    	#for each of the element
        for i in range(n):
        	# before the last element
            if n-i > 1: #cannot equal to 1, because range(n) doesn't include the n_th element
            	# the i_th element = (i-2)th + (i-1)th
                dp[i] = dp[i-1]+dp[i-2] #re-asign value to the i_th element
            else:
                dp[i] = dp[i-1]
        return(dp[-1])


    # second time - still DP [24ms + 13.1MB (99.62% + 74.92%)]
    def climbStairs(n):
        curr = prev = 1
        for i in range(n-1):
            curr, prev = curr + prev, curr
        return curr