class Solution:
	# my method, algorithm inspired by chinese official explanation (not code)
	# 44ms + 13.2 MB (73.04% + 37.62%)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums[::-1] == sorted(nums):
            nums[::] = nums[::-1]
        else:
            i = len(nums) - 1
            while i > 0:
                if nums[i] > nums[i-1]:
                    mut = nums[i-1]
                    rng = [j for j in nums[i+1:len(nums)] if j > mut]

                    if rng:
                        mut2 = min(rng)
                        mut2_ind = i + rng.index(mut2)+1
                        print(mut2_ind)
                        # exchange
                        temp = nums[i-1]
                        nums[i-1] = nums[mut2_ind]
                        nums[mut2_ind] = temp
                        # re-rank
                        nums[i:len(nums)] = sorted(nums[i:len(nums)])
                        break
                    else:
                        temp = nums[i-1]
                        nums[i-1] = nums[i]
                        nums[i] = temp
                        print(i)
                        nums[i:len(nums)] = sorted(nums[i:len(nums)])
                        break
                i -= 1






            
        