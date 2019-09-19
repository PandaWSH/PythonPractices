class Solution:
	# my method 44ms, 13.3MB (47.30% + 12.26%)
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        i = 0
        while i < len(s):
            if s[i] != t[i]:
                return t[i]
            i+=1
        return t[-1]