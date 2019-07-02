class Solution:
	# method 1 -- with math library imported
    def mySqrt1(self, x: int) -> int:
        import math
        result = math.sqrt(x)
        b = str(result).split('.')
        return int(b[0])

     # method 2 -- not using math library
         def mySqrt2(self, x: int) -> int:
         	# sqrt() would be expressed as **0.5
        result = str(x ** 0.5)
        r = result.split('.')
        return int(r[0])

    # second time - binary search
    def mySqrt(self, x):
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = (left + right) >> 1 # same as int( (left + right)/2 )
            if mid * mid > x:
                right = mid
            elif mid * mid < x:
                if mid == left:
                    return mid
                left = mid
            else:
                return mid
        return None