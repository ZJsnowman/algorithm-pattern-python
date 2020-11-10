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

    # 快排 时间复杂度度 O(nlogn)
    def quick_sort(self, nums):
        if len(nums) < 2:
            return nums
        else:
            pivot_index = 0
            pivot = nums[pivot_index]
            less_part = [i for i in nums[pivot_index + 1:] if i < pivot]
            great_part = [i for i in nums[pivot_index + 1:] if i >= pivot]
            return self.quick_sort(less_part) + [pivot] + self.quick_sort(great_part)

    def quick_sort_inplace(self, nums, start, end):  # 左闭右开
        if start < end:
            pivot = self.partition(nums, start, end)
            self.quick_sort_inplace(nums, start, pivot)
            self.quick_sort_inplace(nums, pivot + 1, end)

        print(nums)

    def partition(self, nums, start, end):
        pivot_index = start
        pivot = nums[start]
        left = start + 1
        right = end - 1

        while True:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] >= pivot:
                right -= 1
            if left > right:
                break
            else:
                nums[left], nums[right] = nums[right], nums[left]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        return right

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        # 合并两个有序数组
        return self.merge(left, right)

    def merge(self, left, right):
        new_sorted_list = []
        i = j = 0
        while (i < len(left) and j < len(right)):
            if left[i] <= right[j]:
                new_sorted_list.append(left[i])
                i += 1
            else:
                new_sorted_list.append(right[j])
                j += 1
        new_sorted_list += left[i:]
        new_sorted_list += right[j:]
        return new_sorted_list


if __name__ == '__main__':
    sol = Solution()
    nums1 = [5, 2, 3, 1]
    nums2 = [5, 1, 1, 2, 0, 0]
    # print(sol.selection_sort(nums1))
    # print(sol.selection_sort(nums2))

    # print(sol.bubble_sort(nums1))
    # print(sol.bubble_sort(nums2))

    # print(sol.quick_sort(nums1))
    # print(sol.quick_sort(nums2))
    # sol.quick_sort_inplace(nums1, 0, len(nums1))
    # sol.quick_sort_inplace(nums2, 0, len(nums2))
    print(sol.merge_sort(nums1))
    print(sol.merge_sort(nums2))
