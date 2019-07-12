class Solution:
	# 1080 ms + 16.9 MB (36.79% + 41.11%) my method, time not good
	def threeSum(self,nums):
		res = []
		nums.sort()
		for cur in range(len(nums)):
			if (cur != 0) and (nums[cur] == nums[cur-1]):
				continue
			two_sum = -nums[cur] #current value
			left = cur + 1 # the value next to current value
			right = len(nums) - 1 #from the right end of the nums list
			while left < right:
				if nums[left] + nums[right] == two_sum:
					res.append([nums[cur], nums[left], nums[right]])
					left += 1 #move inward
					right -= 1 # move inward
					while (left < right) and (nums[left] == nums[left-1]):
						left += 1 #after moving inward, if it's the same, move to next
					while (left < right) and (nums[right] == nums[right+1]):
						right -= 1
				elif nums[left] + nums[right] > two_sum:
					right -= 1
				else:
					left += 1
		return res

	# method 2 420ms + 17.1MB (97.37% + 28.32%)
	# divide the numbers in nums into three groups: positive, negative, zero
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set([]) 
        plus = sorted([n for n in nums if n>0]) #the positive numbers in nums
        plus_c = set(plus)

        zero = [n for n in nums if n == 0] # zeros in nums

        minus = sorted([n for n in nums if n<0]) #the negative numbers in nums
        minus_c = set(minus)
        # all zero
        if len(zero)>2:
            result.add((0,0,0))
        # plus zero minus
        if len(zero)>0:
            for n in minus:
                if -n in plus_c:
                    result.add((n,0,-n))
        # plus minus minus
        m = len(minus)
        for i in range(m): # current value in negative group
            for j in range(i+1,m): # all the rest values in the negative groups
                diff = -(minus[i]+minus[j])
                if diff in plus_c:
                    result.add((minus[i],minus[j],diff))

        # plus plus minus
        p = len(plus)
        for i in range(p):
            for j in range(i+1,p):
                diff = -(plus[i]+plus[j])
                if diff in minus_c:
                    result.add((diff,plus[i],plus[j]))
        return list(result)

        #method three time exceed
        '''
		in this method, instead of initialize result as set([]), it was initialized as [], and "add" function was
		replaced by "append".
		in addition, in the final section, following code was added
			diction = {}
			for i in range(len(result)):
			    if result[i] not in diction.values():
			        diction[i]=result[i]
			    else:
			        pass
			return list(diction.values())
		However, this method had time limit exceed problem
		'''


		# second time - same as method 2, minor expression difference
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        positive = []
        negative = []
        zero = []
        for i in nums:
            if i > 0:
                positive.append(i)
            elif i < 0:
                negative.append(i)
            else:
                zero.append(i)
        positive = sorted(positive)
        negative = sorted(negative)
        pos_set = set(positive)
        neg_set = set(negative)
        result = set([])
        
        if len(zero) > 2:
            result.add((0,0,0))
        if len(zero) > 0:
            for n in negative:
                if -n in pos_set:
                    result.add((0,n,-n))
        # --+
        n = len(negative)
        for i in range(n):
            for j in range(i+1,n):
                diff = 0-negative[i]-negative[j]
                if diff in pos_set:
                    result.add((negative[i],negative[j],diff))
        # ++-
        p = len(positive)
        for i in range(p):
            for j in range(i+1,p):
                diff = 0 - positive[i]-positive[j]
                if diff in neg_set:
                    result.add((positive[i],positive[j],diff))
        return list(result)
        