class Solution(object):
    # my method 40ms + 12.2 MB (86.99% + 23.46%)
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) == 0:
            return True
        magazine = list(magazine)
        i = 0
        while i < len(ransomNote):
            try: 
                magazine.remove(ransomNote[i])
                i += 1
            except: 
                return False
        return True