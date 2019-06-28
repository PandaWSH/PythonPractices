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

    # inspired online 91.89% method, improved to 99.94% fast (24ms + 13.2 MB [44.50%])
    def longestCommonPrefix(self, strs):
        # empty strs
        if not strs: return "" 

        # the length of min sub-string
        l = len(min(strs, key=len))
        #modify the string: cut all string in the list to the shortest length
        strs= [s[:l] for s in strs]

        # while no empty string
        # --- recursive ---
        while len(min(strs, key=len)) > 0: # when there's no empty string
            # base line (break): when all same string, set() convert the list to single string list
            if len(set(strs)) == 1: 
                return strs[0]
            else:
                # otherwise, remove the last character from each string
                strs = [ s[:-1] for s in strs]
        return ""


    # method 3, 28ms + 13.4MB ( 99.33% + 10.07%) 借助ASCII的的default排序，只用比较最大最小的common
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

    # method 4, 36ms + 13.4MB (86.7% + 5.6%)
    # zip(*list), set, 
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        
        new_strs = list(zip(*strs))
        if len(new_strs) == 0:
            return ""
        l = len(new_strs)
        result = "" 
        
        for i in range(l):
            if len(set(new_strs[i])) == 1:
                result += new_strs[i][0]
            else:
                break
        return result
            
                
                