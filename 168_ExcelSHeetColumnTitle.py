class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n  > 0:
            if n % 26 == 0:                
                result = 'Z' + result
                n = int(n/26) - 1
            else: 
                # find the character for reminder
                result = chr(n % 26+64) + result
                # find the times of full loop, to find the tenth digit num
                n = int(n/26)
        return 
        