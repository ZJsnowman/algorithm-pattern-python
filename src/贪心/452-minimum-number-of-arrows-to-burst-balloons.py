# -*- coding: utf-8 -*-
class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        贪心一般用来解决"找到要做某事的最小数量"或者"找到在某些情况下适合的最大物品数量"，且提供的是无序的输入
        贪心算法的思想是每一步都选择最佳的解决方案，最终获得全局最佳的解决方案。一般使用反证法证明
        贪心
        求不重叠的区间个数，同435

        :param points:
        :return:
        """
        if len(points)<=1:
            return len(points)
        points.sort(key=lambda x:x[1])
        end = points[0][1]
        result = 1
        for point in points[1:]:
            if point[0]>end:
                end = point[1]
                result+=1
        return result