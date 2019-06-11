class Solution(object):
	# my method
    def addDigits(self, num):
    	# <9 means this number has only one digit (assume input >=0)
        if num <= 9:
            return num
        
        while num > 9:
            s_num = str(num)
            num = sum([int(i)for i in s_num])
            
        return num