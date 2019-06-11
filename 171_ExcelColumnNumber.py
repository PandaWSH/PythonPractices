class Solution(object):

    #my own method 16ms + 11.8 MB
    def titleToNumber(self, s):

        if len(s) == 1:
            return ord(s) - 64           
        else: # two digit
            pos = len(s) - 1
            value = (ord(s[pos]) - 64) 
            while pos > 0:
                value += (ord(s[pos-1]) - 64) * 26 **(len(s)-pos) 
                pos -= 1
            return value