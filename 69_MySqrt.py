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