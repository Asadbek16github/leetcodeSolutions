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



# Aproach 2 
class Solution2:
    def mergeKLists(self, lists):
        if len(lists) == 0: return None

        while len(lists) > 1:
            merge = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else None
                merge.append(self.Merge_Two_List(l1, l2))
            lists = merge
        return lists[0]

    def Merge_Two_List(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2

        return dummy.next