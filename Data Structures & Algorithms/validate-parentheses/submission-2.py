class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        map1 = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        stack1 = []

        for c in s:
            if c == '{' or c == '(' or c == '[':
                stack1.append(c)
            elif len(stack1) == 0 or map1[c] != stack1.pop():
                return False
        
        if len(stack1) == 0:
            return True
        else:
            return False # stack1 is empty