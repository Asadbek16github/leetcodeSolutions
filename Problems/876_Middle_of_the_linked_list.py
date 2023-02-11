# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(head):

        mid = 0
        p = head
        q = head
        while q and q.next:
            p = p.next
            q = q.next.next
            mid+=1

        result_list = head
        while mid:
            result_list = result_list.next
            mid-=1
        
        return result_list