class Solution:
	# time exceed
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == 0:
            return 0
        if divisor == 1 and dividend < 2*31-1 and dividend > -2**31:
            return dividend
        if divisor == -1 and -dividend < 2*31-1 and -dividend > -2**31:
            return -dividend
        
        counter = 0
        absor = abs(divisor)
        abdend = abs(dividend)
        bas = 0 + absor
        if absor < absor:
            return 0
        else:
            while bas <= abdend:
                counter += 1
                bas += absor
        print(counter)        
        if counter < 2**31-1 and -counter > -2*31:
            if divisor > 0 and dividend > 0 :
                return counter
            elif divisor < 0 and dividend < 0:
                return counter
            else:
                return -counter
        else:
            return 2**31-1


    # binary search 32ms + 13.1 MB ( 96.37% + 86.84%  )
	def divide(self, dividend, divisor):
	    """
	    :type dividend: int
	    :type divisor: int
	    :rtype: int
	    """
	    ncount,flag,res=0,1,0
	    # different sign
	    if (divisor<0 and dividend>0) or (divisor>0 and dividend<0):
	        flag=-1

	    divisor,dividend=abs(divisor),abs(dividend)
	    # special case
	    if divisor>dividend:return 0

	    while dividend>=divisor:
	        tmp=divisor
	        ncount=1
	        while tmp<=dividend:
	            dividend-=tmp
	            res+=ncount
	            tmp+=tmp
	            ncount+=ncount

	    #consider the overflow, even though python3 didn't consider
	    if res*flag<-2147483648:return -2147483648
	    elif res*flag>2147483647:return 2147483647
	    else: return res*flag

	        
	            
	        