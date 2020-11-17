# -*- coding: utf-8 -*-
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        贪心算法。
        在不重叠的前提下，尽可能多的保留下区间。然后用总区间数减去得出的区间数就是最少需要丢掉的区间
        这样问题就转换成如何尽可能多的保留区间切区间之间不重叠。
        1.先按照区间的末尾进行排序
        2.在每次选择中，区间的结尾最为重要，选择的区间结尾越小，留给后面的区间的空间越大，那么后面能够选择的区间个数也就越大。
        :param intervals:
        :return:
        """
        if len(intervals) <= 1:
            return 0
        intervals.sort(key=lambda x: x[1])  # 按照区间末尾进行排序
        result = 1
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= end:  # 因为已经按照区间末尾排序了，这里只需选择区间开始不小于上一 end的即可
                result += 1
                end = interval[1]  # 更新 end
        return len(intervals) - result
