# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next





# Aproach 1
class Solution:
    def mergeNodes(self, head):
        l, r = head, head.next

        while r:
            if l.val == 0:
                r = r.next
                l = l.next

            if r.val == 0:
                l.next = r.next
                l = l.next
                r = l.next if l else None
            
            else:
                l.val = l.val + r.val
                r = r.next
                l.next = r

        return head.next
    

# Aproach 2
class Solution:
    def mergeNodes(self, head):
        l, r, counter = head, head.next, 0

        while r:
            
            if r.val == 0:
                l.val = counter
                counter = 0
                if r.next:
                    l = l.next
                else:
                    l.next = None
            else:
                counter += r.val

            r = r.next

        return head