class Solution:
    def isValid(self, s: str) -> bool:
        map1 = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        stack = []
        for c in s:    
            if c in ('{', '(', '['):
                stack.append(c)   
            else:
                if stack and map1[c] == stack[-1]:
                    stack.pop()
                    
                else:
                    return False
                
        
        return not stack

        