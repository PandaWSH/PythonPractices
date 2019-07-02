class Solution:
	#My own method 40ms
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
 
 	# Method shared by pthers 40ms
    def merge2(self, nums1, m, nums2, n):
    	#directly cover part of nums1 with nums2
        nums1[m:] = nums2[:]
        nums1.sort()


    # second time -not using built-in sort() function
    # 32ms + 13.2MB [97.31% + 34.96%]
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Do not return anything, modify nums1 in-place instead."""
        
        if not nums2:
            nums1
        elif not nums1:
            nums1[:] = nums2[:]

        i1 = 0
        i2 = 0
        while i1 < m and i2 < n:
            if nums2[i2] <= nums1[i1]: #need to insert this nums2 into nums1
                nums1[i1+1:m+1] = nums1[i1:m] #把现在的nums1整体后移一位
                m += 1 #update新nums1的长度
                nums1[i1] = nums2[i2] #把较小的这一个nums2的值放在nums1里
                i1 += 1 #由于nums1已经整体后移了，所以要继续比较这个数的话，i1也需要+1
                i2 += 1 #比较下一个nums2的数字
            else:
                i1 += 1
        if i2 < n:
            nums1[m:] = nums2[i2:]
            