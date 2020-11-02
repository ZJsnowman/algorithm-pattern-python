# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while (slow and fast and fast.next):  # 其中有一个为 None则中断循环
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False
