# -*- coding: utf-8 -*-
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l= 0
        r = int(c**0.5)+1
        while (l<=r):
            result = l**2+r**2
            if result ==c:
                return True
            elif result<c:
                l=l+1
            else:
                r=r-1
        return False