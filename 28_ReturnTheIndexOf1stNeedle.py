class Solution:
	# second time - fast time complexity O(1)
	# 32 ms + 13.3 MB ( 93.46% + 65.26%)
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1

    # 48ms + 13.3 MB (30.41% + 71.43%)
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        h,n = len(haystack),len(needle)
        for i in range(h):
            if haystack[i:i+n] == needle:
                return i
        return -1

            