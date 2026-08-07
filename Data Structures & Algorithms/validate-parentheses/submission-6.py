class Solution:
    def isValid(self, s: str) -> bool:
  
            
        validation = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }
        stack1 = []
        for c in s:
            if c in ['(', '[', '{']:
                stack1.append(c)
            elif c in [')', ']', '}']:
                if not stack1 or validation[c] != stack1.pop():
                    return False

                
        return not stack1
