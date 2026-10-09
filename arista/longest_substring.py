#LC 3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        max_len = 1
        left, right = 0, 1
        have_seen = {s[0]}

        while right < len(s):
            while s[right] in have_seen:
                have_seen.remove(s[left])
                left += 1

            have_seen.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("baaabca"))
    pass