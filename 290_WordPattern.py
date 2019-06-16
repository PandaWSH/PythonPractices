class Solution:
    # my method, 20ms + 13.1MB(100% + 78.52%)
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern:
            return False
        
        str_list = str.split(" ")
        p_list = list(pattern)
        
        #determine if str and pattern was in the same format
        # ------------ same method used in #205 -----------
        diction = {}
        if len(p_list) != len(str_list):
            return False
        for i in range(len(p_list)):
            if p_list[i] not in diction:
                if str_list[i] not in diction.values():
                    diction[p_list[i]] = str_list[i]
                else:
                    return False
            elif p_list[i] in diction:
                if diction[p_list[i]] != str_list[i]:
                    return False
        return True