class Solution:
	# my method, use intersection fuction 36ms + 13.2 MB (92.96% + 78.05%)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 == [] or nums2 == []:
            return []
        return list(set(nums1).intersection(set(nums2)))


    # method shared online
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        nums1.sort()
        nums2.sort()
        i, n1 = 0, len(nums1)
        j, n2 = 0, len(nums2)
        ans, last = [], None
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                if nums1[i] != last:
                    ans.append(nums1[i])
                    last = nums1[i]
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
        return ans