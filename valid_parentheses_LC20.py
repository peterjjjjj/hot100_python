class Solution:
    def isValid(self, s: str) -> bool:
        """
        TC: O(n)
        SC: O(1)
        :param s:
        :return:
        """

        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []


        for char in s:
            if char not in bracket_map:
                stack.append(char)

            else:
                if not stack or bracket_map[char] != stack.pop():
                    return False

        return not stack

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("()[]{}"))