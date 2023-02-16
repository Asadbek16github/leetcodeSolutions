# The first solution is creating new Linked List


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import math
class Solution:
    def mergeTwoLists(self, list1, list2):
        result = ListNode(0)
        start = result
        

        while list1 or list2:
            if not list1:
                a = math.inf
            else:
                a = list1.val
            
            if not list2:
                b = math.inf
            else:
                b = list2.val

            
            if(a<=b):
                start.next = ListNode(a)
                list1 = list1.next
            elif(a>b):
                start.next = ListNode(b)
                list2 = list2.next
            start = start.next

        return result.next
    

