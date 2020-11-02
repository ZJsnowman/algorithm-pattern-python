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


if __name__ == '__main__':
   a=[22,22,22,22]
   b=[]
   start = len(a)-1
   for i in range(len(a)):
       index=start-i
       b.append(a[index])
print(b)
