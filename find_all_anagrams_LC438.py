import string

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        TC = O(n)
        SC = O(1)
        :param s:
        :param p:
        :return:
        """

        if not s or not p:
            return []
        if len(p) > len(s):
            return []

        p_count = [0] * 26
        s_count = [0] * 26
        output = []

        for char in p:
            p_count[ord(char) - ord('a')] += 1

        window_length = len(p)
        i = 0

        for right in range(len(s)):

            s_count[ord(s[right]) - ord('a')] += 1

            if right >= window_length:
                left_char = s[right - window_length]
                s_count[ord(left_char) - ord('a')] -= 1

            if right >= window_length - 1:
                if s_count == p_count:
                    output.append(right - window_length + 1)

        return output


if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams(s="abc", p="abc"))


