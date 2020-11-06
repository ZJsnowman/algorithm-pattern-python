# -*- coding: utf-8 -*-

class Solution:
    # 选择排序 时间复杂度O（n^2） 空间复杂度 O(1)
    def selection_sort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    # 冒泡排序  时间复杂度O(n^2) 空间复杂度 O(1)
    def bubble_sort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    def quick_sort(self, nums):
        if len(nums) < 2:
            return nums
        else:
            pivot_index = 0
            pivot = nums[pivot_index]
            less_part = [i for i in nums[pivot_index + 1:] if i < pivot]
            great_part = [i for i in nums[pivot_index + 1:] if i >= pivot]
            return self.quick_sort(less_part) + [pivot] + self.quick_sort(great_part)


if __name__ == '__main__':
    sol = Solution()
    nums1 = [5, 2, 3, 1]
    nums2 = [5, 1, 1, 2, 0, 0]
    # print(sol.selection_sort(nums1))
    # print(sol.selection_sort(nums2))

    # print(sol.bubble_sort(nums1))
    # print(sol.bubble_sort(nums2))

    print(sol.quick_sort(nums1))
    print(sol.quick_sort(nums2))
