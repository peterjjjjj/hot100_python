class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        left = 0
        have_seen = set()
        longest = 0

        for right in range(len(s)):
            curr_char = s[right]

            while curr_char in have_seen:
                have_seen.remove(s[left])
                left += 1

            have_seen.add(curr_char)

            longest = max(longest, right - left + 1)

        return longest



if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("bbbbb"))