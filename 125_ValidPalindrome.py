class Solution:
    # method by my own, 79.96%
    def isPalindrome(self, s: str) -> bool:
        # empty or single string
        if not s or len(s) == 1:
            return True
        else:
            #convert into pure character/number without space: string s_noSpace
            import string
            s = ''.join(c for c in text if c not in string.punctuation)
            s = s.lower()
            s = s.split(' ')
            s_noSpace = ''
            for i in s:
                s_noSpace = s_noSpace + i
            # length l for future use    
            l = len(s_noSpace)
            
            # judge
            if l % 2 != 0: #non-symmetric
                #mid = int((l-1)/2)
                left = s_noSpace[0:int((l-1)/2)]
                right = s_noSpace[::-1][0:int((l-1)/2)]
                if left == right:
                    return True
                else:
                    return False
            else: #symmetric
                left = s_noSpace[0:int(l/2)]
                right = s_noSpace[::-1][0:int(l/2)]
                if left == right:
                    return True
                else:
                    return False
                    
    # method 2, shared online, 100%, good and fast
    # reflected that I OVERTHOUGHT for my own method 1
    def isPalindrome(self, s):
        s = re.sub(r'\W', '', s).upper()
        return s == s[::-1]