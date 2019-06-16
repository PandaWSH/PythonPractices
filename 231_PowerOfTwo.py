class Solution:
	# my method, binary
	# 32 ms + 13.5 MB
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        bi = list(bin(n)[2:])
        bi.pop(0)
        if set(bi) == {'0'}:
            return True
        else:
            return False
    # 36ms + 13.1 MB
    def isPowerOfTwo(self.n):
	    if n <= 0:
	    	return False

	    while n % 2 == 0:        	
	    	n = n / 2

	    return n == 1