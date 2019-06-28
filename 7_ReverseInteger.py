class Solution:
    # my method 1: convert to string, reverse and then convert back
    # 36ms + 13.3 MB (85.06% + 34.83%)
    def reverse(self, x):
        if x < -2**31 or x > 2**31-1 or x == 0:
            return 0

        else:
            if x > 0 :
                result = int(str(x)[::-1])
                if result <= 2**31-1:
                    return result 
                else: return 0
            else:
                result = int(str(abs(x))[::-1])
                if result <= 2**31: return -1*result 
                else: return 0

    # my method 2: add up numbers in reverse order
    # 32ms + 13.3MB (95.33% + 28.32%)
    def reverse(self, x):
        if x == 0:
            return 0
        elif x > 0:
            flag = 1
        else:
            flag = -1
            x = abs(x)
            
        x = list(str(x))
        l = len(x) #10**(l-1)
        num = 0
        for i in range(l):
            num += int(x.pop(0)) * 10**(i)
        
        result = flag*num
        if result < 2**31-1 and result > -2**31:
            return flag*num
        else:
            return 0