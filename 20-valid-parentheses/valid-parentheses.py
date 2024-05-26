class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Symbols = {')': '(', ']': '[', '}': '{'}
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if stack == [] or stack[-1] != Symbols[s[i]]:
                    return False
                stack.pop()
        if stack == [] :
            return True
        else:
            return False

            