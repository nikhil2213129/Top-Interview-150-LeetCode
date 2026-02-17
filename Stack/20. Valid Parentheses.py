class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openbracket = "({["
        check = {")":"(","}":"{","]":"["}
        stack = []
        for i in s:
            if i in openbracket:
                stack.append(i)
            else:
                if len(stack) != 0:
                    length = len(stack)
                    if stack[length-1] == check[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0
