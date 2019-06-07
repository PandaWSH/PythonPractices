class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #convert from input string to decimal, then sum up
        result = int(a,2) + int(b,2)
        #convert the decimal result to binary string, remove '0b'
        return str(bin(result))[2::]