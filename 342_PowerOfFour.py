class Solution:
    # my method 28ms+13.1MB (99.24% + 87.70%) 
    def isPowerOfFour(self, num: int) -> bool:
        if num>2**31-1 or num<0:
            return False
        if num == 1:
            return True
        elif num % 4 != 0 or num==0:
            return False
        else:
            while num % 4 == 0:
                num = num/4
            return True if num== 1 else False