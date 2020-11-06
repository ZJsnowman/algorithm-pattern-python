# -*- coding: utf-8 -*-
class Solution:
    def findLongestWord(self, s: str, d) -> str:
        lst = ''
        for sub in d:
            i = j = 0
            while (i < len(s) and j < len(sub)):
                if s[i] == sub[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(sub):   # 满足即为子字符串
                if len(sub) > len(lst):
                    lst = sub
                elif len(sub) == len(lst):
                    if sub < lst:   # 相同长度返回字典顺序
                        lst = sub
        return lst
