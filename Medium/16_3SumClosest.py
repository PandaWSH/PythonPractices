class Solution:
    #my method: time exceed
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) <= 3:
            return sum(nums)
        
        nums=sorted(nums)
        
        if target <= sum(nums[0:3]):
            return sum(nums[0:3])
        elif target >= sum(nums[-3:]):
            return sum(nums[-3:])
        
        resultset = set()
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    summ = nums[i]+nums[j]+nums[k]
                    resultset.add(summ) 
                    
        resultset=sorted(list(resultset))

        for i in range(len(resultset)-1):
            if resultset[i] == target:
                return resultset[i]
            elif resultset[i] < target and resultset[i+1] > target:
                if target - resultset[i] > resultset[i+1] - target:
                    return resultset[i+1]
                else:
                    return resultset[i]
    #online method
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        # ensure diff as a postive integer, so don't need use abs().
        diff = target - res if target > res else res - target
        
        
        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                # skip adjadcent duplicates
                continue
                
            l, r = i + 1, len(nums) - 1
            if nums[i] + nums[r-1] + nums[r] <= target:
                # compare with the largest subset
                
                s = nums[i] + nums[r-1] + nums[r]
                if s == target:
                    return s

                if target - s < diff:
                    res = s
                    diff = target - s

            elif nums[i] + nums[l] + nums[l+1] >= target:
                # compare with the smallest subset
                
                s = nums[i] + nums[r-1] + nums[r]
                if s == target:
                    return s

                if s - target < diff:
                    res = s
                    diff = s - target
            else:
                while l < r:
                    s = nums[i] + nums[l] + nums[r]

                    if s == target:
                        return s
                    elif s < target:
                        l += 1
                        if target - s < diff:
                            res = s
                            diff = target - s
                    else:
                        r -= 1
                        if s - target < diff:
                            res = s
                            diff = s - target
        return res