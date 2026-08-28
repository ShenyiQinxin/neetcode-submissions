class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        stack = []
        for c in s:
            if c in ('{', '[', '('):
                stack.append(c)
            else:
                if stack and stack[-1] == paren_map.get(c):
                    stack.pop()
                else:
                    return False
        return not stack

            
        