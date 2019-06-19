    # my method 36ms + 13.1MB ( 76.80% + 61.10%)
    def getSum(self,a,b):
        return sum([a,b])
        
    # online method 32ms + 13.3MB (90.86% + 23.09%)
    def getSum(self, a, b):
        def add(a, b): 
            if not a or not b:
                return a or b
            return add(a^b, (a&b) << 1)

        if a*b < 0: # assume a < 0, b > 0
            if a > 0:
                return self.getSum(b, a)
            if add(~a, 1) == b: # -a == b
                return 0
            if add(~a, 1) < b: # -a < b
                return add(~add(add(~a, 1), add(~b, 1)),1) # -add(-a, -b)

        return add(a, b) # a*b >= 0 or (-a) > b > 0 