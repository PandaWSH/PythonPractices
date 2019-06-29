class Solution:
    # second time - my method, 36ms + 13.4MB (81.58% + 5.11%) 
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)


    # same as the first one, but use "del function"
    def removeElement(self, nums: List[int], val: int) -> int:
        ini = 0
        while ini < len(nums):
            if nums[ini] == val:
                del nums[ini]
            ini+=1
        return len(nums)


    # online method : two pointers
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[count] = nums[i]
                count +=1
        return count

    # Time complexity: https://wiki.python.org/moin/TimeComplexity