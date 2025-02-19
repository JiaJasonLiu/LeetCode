# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)

        length = len(merged)
        if length % 2 == 0:
            lower_mid = math.floor(length / 2) - 1
            upper_mid = math.floor(length / 2)
            print(lower_mid, upper_mid)
            return (merged[lower_mid] + merged[upper_mid]) / 2
        
        return (merged[int(length / 2)])

# not fast enough with

# Potential TODO: Merge Sort, Two-Pointer, Binary Search
# But I believe my method to be more readable and simpler
# Binary Search -> don't fully understand it