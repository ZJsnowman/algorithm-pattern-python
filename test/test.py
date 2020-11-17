# -*- coding: utf-8 -*-

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start:start + L] == needle:
                return start
        return -1


class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def f(self):
        return "Hello World"


class Dog:
    kind = []  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance

    def chang_kind(self, newKind):
        self.kind.append(newKind)


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


class Recursive:

    def factorial(self, n):
        """
        阶乘
         factorial(n)=factorial(n-1)*n
         factorial(1)=1
        :param n:
        :return:
        """

        if n == 1:
            return 1
        return self.factorial(n - 1) * n

    def fabnocacci(self, n):
        """
        斐波拉契数列
        1,1,2,3,5,8,13,21
        fabnocacci(n)=fabnocacci(n-1)+fabnocacci(n-2)
        fabnocacci(1)=1
        fabnocacci(2)=1
        :param n:
        :return:
        """
        if n <= 2:
            return 1
        return self.fabnocacci(n - 1) + self.fabnocacci(n - 2)


if __name__ == '__main__':
    recur = Recursive()
    # print(recur.factorial(1000j))

    print(recur.fabnocacci(5))
