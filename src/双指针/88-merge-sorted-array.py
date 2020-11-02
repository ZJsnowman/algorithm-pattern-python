# -*- coding: utf-8 -*-
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        l1 = m - 1
        l2 = n - 1
        k = m + n - 1
        while (l1 >= 0 and l2 >= 0):
            if nums1[l1] < nums2[l2]:
                nums1[k] = nums2[l2]
                k -= 1
                l2 -= 1
            else:
                nums1[k] = nums1[l1]
                k -= 1
                l1 -= 1
        while (l2 >= 0):
            nums1[k] = nums2[l2]
            k -= 1
            l2 -= 1
        return nums1


if __name__ == '__main__':
    s = Solution()
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(s.merge(nums1, m, nums2, n))
