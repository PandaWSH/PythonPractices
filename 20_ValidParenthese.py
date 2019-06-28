class Solution:
    # Both are stack methods

    # method 1: 36ms + 13.3 MB
    def isValid(self, strs: str) -> bool:
        p = {')':'(', ']':'[', '}':'{'}
        checkp = [1] #the stack
        for i in strs:
            if i in p and p[i] == checkp[len(checkp)-1]:
                checkp.pop()
            else:
                checkp.append(i)
        return len(checkp) == 1

    # method 2: 32ms + 13.2 MB (93.81% + 65.79%)
    # from chinese official website，the animation helped understanding
    def isValid(self, strs):
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}

        for char in strs:
            if char in mapping:
                top_element = stack.pop() if stack else '#' '''有可能在stack为空时出现了一个反括号，此时记作任意符号
                                                            这个任意符号在下一个mapping[char]判定里也会lead出break'''    

                # Directly break condition
                if mapping[char] != top_element:
                        return False

            else:
                stack.append(char)
        return not stack


            
                
                