# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, numbers, target):
        l = 0
        r= len(numbers)-1
        if not numbers:
            return []
        while (l<r):
            result = numbers[l]+numbers[r]
            if result==target:
                return [l+1,r+1]
            elif result >target:
                r=r-1
            else:
                l=l+1
        return [-1,-1]

if __name__ == '__main__':
    s=Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(numbers,target))