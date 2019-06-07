class Solution:
	#My own method
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # truncate the nums1 array to m length
        del nums1[m:m+n]
        # append all nums2 to nums1 (assume enough space)
        for i in range(n):
            nums1.append(nums2[i])
        # sort the result in objective order
        nums1.sort()
 
 	# Method shared by pthers
    def merge2(self, nums1, m, nums2, n):
    	#directly cover part of nums1 with nums2
        nums1[m:] = nums2[:]
        nums1.sort()