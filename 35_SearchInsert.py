class Solution:
    # Method 1
    def searchInsert1(self, nums, target):
        # empty string OR target smaller than all
        if len(nums) == 0 or target < nums[0]:
            return 0
        # target greater than all
        elif target > nums[-1]:
            return len(nums)
        else:
            try:
                #find the match index
                return nums.index(target)
            except:
                #target us in between two values
                for num in nums:
                    if num - target > 0:
                        return nums.index(num)+1

    # Method 2
    def searchInsert2(self, nums, target):
        try:
            #find the match index
            return nums.index(target)
        except:
            #if no match
            # empty string or smaller target than the 1st number in string
            if len(nums) == 0 or target < nums[0]:
                return 0
            ind = 0

            while ind < len(nums):
                # if the target was found smaller than some value
                if nums[ind] > target:
                    # return that index because target 
                    # would replace that value
                    return ind
                ind += 1
            return len(nums)
            
    # Method 3 -- Shared by someone online, used Binary Search Method
    def searchInsert3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        if not nums:
            return 0
        
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
                
        if target > nums[mid]:
            return mid + 1
        else:
            return mid