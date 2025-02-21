# https://leetcode.com/problems/longest-palindromic-substring/description/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        maxPal = ""
        subStrings = []
        for left in range(len(s)):
            for right in range(left, len(s)):
                subString = s[left:right + 1]
                mid = (right - left) / 2
                mid1 = mid2 = int(mid)
                
                if len(subString) % 2 == 0:
                    mid1 += 1
                
                if subString[0 : mid1] == subString[mid2 + 1:][::-1]:
                    if len(subString) >= len(maxPal):
                        maxPal = subString

        return maxPal

# Making it faster
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str

# expand from the center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        hello = "dwjadiwajdijwaidjaw"
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str