class Solution(object):
# my method 1: 52ms + 13.3MB (13% + 15.49%)
# straight forward method, determing if the floating result == integer result
    def isPerfectSquare(self, num):
        return int(num**0.5) == num** 0.5

# my method 2: 64ms + 13.4MB (5.82%)
# search one by one starting from zero
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        while i**2 < num:
            i+=1
        
        if i**2 == num:
            return True
        else:
            return False

# me method 3: 48ms + 13.2MB
# similar to method 2, but shrinked size
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        while i < num**0.5:
            i+=1
        
        if i**2 == num:
            return True
        else:
            return False

# online method shared(40ms + 13MB)37.32% + 88.78%:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<0:
            return False
        x,i=0,1
        while x<num:
            x+=i
            i+=2
        return x==num
