class Solution:
    # my method Hashtable 108ms + 13.4 MB (78.77%+19.15%)
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        """
        :type s: str
        :rtype: int
        """
        diction = {}
        for i in s:
            if i not in diction:
                diction[i] = 1
            else:
                diction[i] = diction[i] + 1
        print(diction)
        for x,y in diction.items():
            if y == 1:
                print(x)
                return s.index(x)
        return -1

    # using collections.Counter
    # 72ms + 13.3 MB (91.50% + 76.71%)
    class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        d = Counter(s)
        for c, count in d.items():
            if count == 1:
                idx = s.index(c) # faster than directly return s.index(c)
                return idx #could also use s.find(c)
        return -1