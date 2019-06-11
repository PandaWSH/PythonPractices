class Solution(object):
    # my method 160ms + 13.3 MB (49.49% + 77.92%)
    def majorityElement(self, nums):
        """
        hashmap + counter(control stop)
        """
        if len(nums) == 1:
            return nums[0]
        else:
            n = len(nums)
            cla = {}
            for i,e in enumerate(nums):
                if e not in cla:
                    cla[e] = 1
                elif e in cla:
                    cla[e] += 1
                    if cla[e] > n/2:
                        return e

    #similarly hashmap
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    # math 144ms + 13.4MB (77.89% + 31.01%)
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]