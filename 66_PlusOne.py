class Solution:
    '''
    My own method of solving problem 66
    '''
    def plusOne(self, digits: List[int]) -> List[int]:
        #initialize index and result
        ind = 1
        result = 0
        while ind <= len(digits):
            #convert current list into a single digit
            result += digits[-ind] * 10**(ind-1)
            ind += 1
        #digit plus one as required
        result = result+1
        
        #convert the result digit back to list [loop]
        fin = []
        while result // 10 >= 1:
            num = result % 10
            fin.append(num)
            result = result // 10
        #append the 1st digit    
        fin.append(result)
        #because of append, the order need to be reversed
        return fin[::-1]
