# 32ms + 13.2MB
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def combine(pres,dicts,digit):
            """
            :type pres:List[str], dicts: dictionary, digits: str
            :rtype: List[str]
            """
            letL=[]
            for pre in pres:
                for letter in dicts[digit]:
                    letL.append(pre+letter)
            return letL
            
        if digits=='':
            return []
            
        dicts={'1':[''], 
               '2':['a','b','c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z'],
               '0':[' ']}
        
        lets=[''] #initialize
        for digit in digits:
            lets=combine(lets,dicts,digit)
        return lets

# using backtrack 44ms + 13.2MB
class Solution:
    dict_of_letters = {
        '2':'abc', 
        '3':'def', 
        '4':'ghi', 
        '5':'jkl', 
        '6':'mno', 
        '7':'pqrs', 
        '8':'tuv', 
        '9':'wxyz'
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        result = []
        self.backtrack('', digits, result)
        return result
    
    def backtrack(self, combination, next_digits, result):
        if len(next_digits) == 0:
            result.append(combination)
        else:
            for letter in self.dict_of_letters[next_digits[0]]:
                self.backtrack(combination + letter, next_digits[1:], result)



# official solution 36ms + 13.2MB(80.04% + 42.22%)
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output
