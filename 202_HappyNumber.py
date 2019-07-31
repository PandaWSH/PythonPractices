#second time 
class Solution:
	#my method 32ms, 13.2 MB (98.67%+ 34.83%)
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False
        
        collect = set()
        n_str = str(n)
        summ = n
        
        while summ not in collect:
            collect.add(summ)
            n_str = str(n)
            summ = sum([int(i)**2 for i in n_str])
            if summ == 1:
                return True
            n = summ
        return False
