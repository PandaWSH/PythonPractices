class Solution(object):
    # my method (56ms + 13.1MB 31.07% + 92.14%)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        result = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                result.append(i)
        return result

    #online method: use diction to count (36ms + 13.3MB 96%+27.02%)
    def intersect(self, nums1, nums2):

        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res

    #online method: use counter to make is cleaner
    # 44ms + 13.1 MB (55.19%+78.71%)
    def intersect(self, nums1, nums2):

        counts = collections.Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return res
