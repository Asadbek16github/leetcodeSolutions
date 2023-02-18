# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

e = ListNode(5)
d = ListNode(4,e)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)


# Solution 1
class Solution:
    def removeNthFromEnd(self, head, n):
        counter = 0
        start = head
        while start:
            counter+=1
            start = start.next
        
        start, stop = 1, counter-n+1
        prev = ListNode(0)
        prev.next = head
        prev2 = prev
        while True:
            if(start==stop):
                if head.next:
                    prev.next = head.next
                else:
                    prev.next = None

                return prev2.next

            prev, head = head, head.next
            start+=1




# Solution 2
class Solution2:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        left, right = dummy, head

        while n:
            right = right.next
            n-=1
        
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next

