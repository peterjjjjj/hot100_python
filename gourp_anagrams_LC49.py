#Doble check this one, done on airplane

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return []

        anagram_map = {}

        for s in strs:
            key = "".join(sorted(s))
            if key in anagram_map:
                anagram_map[key].append(s)
            else:
                anagram_map[key] = [s]

        return list(anagram_map.values())


if __name__ == "__main__":
    test = Solution()
    print(
        test.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    )
