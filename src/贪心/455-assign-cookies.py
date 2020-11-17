# -*- coding: utf-8 -*-
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        m= n = 0
        while (m<len(g) and n <len(s) ):
            if g[m]<=s[n]:
                m+=1
                n+=1
            else:
                n+=1
        return m

