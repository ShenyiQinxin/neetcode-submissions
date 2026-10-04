class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = set(['-', '+', '*', '/'])
        stack = []

        for c in tokens:
            if c in op:
                b = stack.pop()
                a = stack.pop()
                n = 0
                if c == '+':
                    n = a + b
                elif c == '-':
                    n = a - b
                elif c == '*':
                    n = a * b
                elif c == '/':
                    n = int(a/b)
                stack.append(n)
            
            else:
                stack.append(int(c))
            
        return stack[-1]

        

        