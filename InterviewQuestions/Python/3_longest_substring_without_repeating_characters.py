# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# My solution -> wrong approach and took too long
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = []
        indexes = []

        for index, c in enumerate(s):
            if c not in subString:
                subString.append(c)
            else:
                indexes.append(index)
        print(subString)
        print(indexes)
        maxNum = 0
        ranges = []
        
        return s

# better answer
#         left = max_length = 0
#         char_set = set()
        
#         for right in range(len(s)):
#             while s[right] in char_set:
#                 char_set.remove(s[left])
#                 left += 1

#             char_set.add(s[right])
#             max_length = max(max_length, right - left + 1)
        
#         return max_length