class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-/*"

        i = 0
        while i < len(tokens):
            token = tokens[i]
            i += 1
            if token not in operators:
                stack.append(token)
                continue
            right = int(stack.pop())
            left = int(stack.pop())
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "/":
                stack.append(left / right)
            else:
                stack.append(left * right)

        return int(stack.pop())