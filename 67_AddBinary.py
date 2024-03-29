class Solution:
	# method 1: 36ms + 13MB
    def addBinary(self, a: str, b: str) -> str:
        #convert from input string to decimal, then sum up
        result = int(a,2) + int(b,2)
        #convert the decimal result to binary string, remove '0b'
        return str(bin(result))[2::]


    # second time - same method but one line, slower and more space
    # 52ms + 13.2 MB
    def addBinary(self, a: str, b: str) -> str:
    	return str(bin(int(a,2) + int(b,2))[2:])
