class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        var = 0
        stack = []
        for sb in s:
            if sb == "(":
                stack.append(var)
                var = 0
            else:
                var = stack.pop() + max(2*var,1)
        return var

        