class Solution:
    # my method 1 (second time): 76ms + 14.9MB [31.77% + 32.29%] 
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            nums
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
                # OR del nums[i]
                # i -= 1 当出现i=-1时，即会比较nums[-1] & nums[0]，由于是sorted array，一头一尾一定不等，会有i+=1
            else:
                i+=1

    # method 2: 52ms + 14.8 MB [96.70% + 60.31%]
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = 0
        # empty
        if not nums:
            return num_count
        
        current_num_and_index = None, -1 #not list, not set, just numbers in array, index callable
        for num in nums:
            if num != current_num_and_index[0]:
                new_index = current_num_and_index[1]+1
                nums[new_index] = num
                current_num_and_index = num, new_index
                num_count += 1
        return num_count #return length of final nums