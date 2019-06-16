class Solution:
    #my method, pair characters in each string to build a dictionary
    # 40ms + 13.3 MB(94.46% + 67.08%)
    def isIsomorphic(self, s: str, t: str) -> bool:
        # special conditions
        if not s and not t:
            return True
        if not s or not t:
            return False
        if len(s) != len(t):
            return False
        
        diction = {}
        for i in range(len(s)):
            if s[i] not in diction:
                if t[i] not in diction.values():
                    diction[s[i]] = t[i]
                else:
                    return False
            elif s[i] in diction:
                if diction[s[i]] != t[i]:
                    return False
        return True