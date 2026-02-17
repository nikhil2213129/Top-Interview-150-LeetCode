class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i in "+-*/":
                value2 = stack.pop()
                value1 = stack.pop()
                if i == "+":
                    stack.append(value1 + value2)
                elif i == "-":
                    stack.append(value1 - value2)
                elif i == "*":
                    stack.append(value1 * value2)
                elif i == "/":
                    stack.append(int(float(value1) / value2))
            else:
                stack.append(int(i))
        return stack[0]
