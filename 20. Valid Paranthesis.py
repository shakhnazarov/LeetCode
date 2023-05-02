# we can use dictionary for brackets to make code shorter
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                stack.pop()
            elif bracket == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                stack.pop()
            elif bracket == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                stack.pop()
            else:
                stack.append(bracket)

        return len(stack) == 0
