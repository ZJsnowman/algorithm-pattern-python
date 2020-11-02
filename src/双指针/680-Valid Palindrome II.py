# -*- coding: utf-8 -*-
class Solution:
    def isPalindrome(self, s, l, r):
        while (l < r):
            if s[l] != s[r]:
                return False
            else:
                l = l + 1
                r = r - 1
        return True

    def isPalindrome2(self, s, l, r):
        a = s[l:r + 1]
        return a == a[::-1]

    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while (l < r):
            if s[l] == s[r]:
                l = l + 1
                r = r - 1
            else:
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)

        return True
