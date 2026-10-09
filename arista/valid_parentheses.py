class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 1:
            return False

        pairs = {'(':')', '{':'}', '[':']'}

        stack = []

        for char in s:
            if char in pairs.keys():
                stack.append(char)
            if char in pairs.values():
                if not stack or char != pairs[stack.pop()]:
                    return False

        return len(stack) == 0