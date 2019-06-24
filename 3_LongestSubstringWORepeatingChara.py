class Solution:
    # my method: hashtable 
    # 104ms + 13.3MB ( 31.72% + 59.36%)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        maxx = []
        currentmax = []
        for i in range(len(s)):
            if s[i] not in maxx:
                maxx.append(s[i])
                currentmax = max(currentmax,maxx,key = len)
            elif s[i] in maxx:
                ind = maxx.index(s[i]) + 1
                maxx = maxx[ind:]
                maxx.append(s[i])
                currentmax = max(currentmax,maxx,key = len)
        print(currentmax)
        return len(currentmax)
        