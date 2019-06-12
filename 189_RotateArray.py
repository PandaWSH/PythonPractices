class Solution:
	#my method 1, 52ms + 13.4MB (89.45% + 61.94%)
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        if k==0: #full rotation, no change
            nums[:]=nums
        else:
            nums[:]=nums[-k::]+nums[0:len(nums)-k]

    #online method 2, using extra array 48ms + 13.6MB (96.43% + 16.40%)
    def rotate2(self, nums, k):
        a = [0] * len(nums)
        for i in range(len(nums)):
            a[(i+k)%len(nums)] = nums[i] #recycle

        for i in range(len(nums)):
            nums[i] = a[i]