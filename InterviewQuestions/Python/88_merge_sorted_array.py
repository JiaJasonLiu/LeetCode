# https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
    

        for i in range(m, m+n):
            nums1[i] = nums2[i - m]
        nums1.sort()