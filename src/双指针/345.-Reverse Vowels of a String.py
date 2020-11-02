# -*- coding: utf-8 -*-
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}  as a set could be faster
        l = 0
        r = len(s) - 1
        result = list(s)
        while (l < r):
            if s[l] not in vowels:
                l = l + 1
            elif s[r] not in vowels:
                r = r - 1
            else:
                result[l], result[r] = s[r], s[l]
                l = l + 1
                r = r - 1

        return "".join(result)


if __name__ == '__main__':
    sol = Solution()
    s = 'hello'
    print(sol.reverseVowels(s))
