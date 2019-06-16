class Solution:
    # method online debugged my problem [NOTE]
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #need counter to count from start of the list
        i = 0
        #counter for subtracting the zero 
        j = len(nums)
        
        
        #checking initial condition
        if len(nums) == 0 or len(nums)==1:
            pass
        else:
            #do the following while i < j
            while i < j:
                # the current element of is 0 then append to the last of the list
                if nums[i] == 0:
                    nums.append(nums.pop(i))
                    #decrement the j
                    j-=1
                    ######## NOTE!!!! CANNOT have i += 1 here
                    ######## because once this nums[i] has been removed, it will automatically take next value
                else:
                    #increment if not zero
                    i+=1

    # my method, occupy few space but slow
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        another = []
        while True:
            try:
                nums.remove(0)
                another.append(0)
            except: #till there's no zero in the string
                break
        nums += another