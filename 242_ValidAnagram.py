class Solution:
    # my method 1 (60ms + 14.2MB)
    def isAnagram(self,s,t):
        return sorter(s) == sorted(t)

    # my method 2 (bad, 1026ms + 13.8 MB)
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        elif len(s) != len(t):
            return False
        ss = list(s)
        #tt = list(t)
        for i in range(len(s)):
            if t[i] in ss:
                ss.remove(t[i])
        return ss == []

    # method shared online (52ms + 13.4 MB)
    def isAnagram(self, s: str, t: str) -> bool:
        if s is None or t is None:
            return False

        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1
                
        if s_dict == t_dict:
            return True

        return False