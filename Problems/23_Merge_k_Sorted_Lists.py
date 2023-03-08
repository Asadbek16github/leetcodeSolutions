# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        val = []
        for i in lists:
            while i:
                val.append(i.val)
                i = i.next

        val.sort()
        res = ListNode(0)
        start = res
        for i in range(len(val)):
            start.next = ListNode(val[i])
            start = start.next

        return res.next