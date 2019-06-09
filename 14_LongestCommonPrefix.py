class Solution(object):
'''
The first two methods were in the same speed,
however, the first one memory is less than 97.91%
while the second one is less than 18.83%
'''

    def longestCommonPrefix(self, strs):
        """
        compare character of each string from the first charactor of the first string
        """
        result = ""
        
        if not strs: return ""
        else:
            # the length of min sub-string
            mi = len(min(strs, key = len))

            # chose the truncate range without storing it!!!!!!!!
            for i in range(mi):
                temp = set([s[i] for s in strs])
                if len(temp) == 1:
                    result += strs[0][i]
                else:
                    break
            return result

    # inspired online 91.89% method, improved to 97.53% fast
    def longestCommonPrefix(self, strs):
        #result output
        ret = ""

        #empty string
        if len(strs) == 0:
            return ret

        # the length of min sub-string
        i = len(min(strs, key=len))
        #modify the string: cut all string in the list to the shortest length
        #works but ocupy additional space??
        strs= [s[:i] for s in strs]

        # while no empty string
        # --- recursive ---
        while len(min(strs, key=len)) > 0: # when there's no empty string
            # base line (break): when all same string, set() convert the list to single string list
            if len(set(strs)) == 1: 
                ret = strs[0]
                break
            else:
                # otherwise, remove the last character from each string
                strs = [s[:-1] for s in strs]
        return ret