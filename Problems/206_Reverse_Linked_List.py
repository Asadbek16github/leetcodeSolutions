# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




# solwing with creating new linked list
class Solution:
    def reverseList(self, head):
        if not head: return None

        res = ListNode(head.val)
        while head:
            if(head.next):
                node = ListNode(head.next.val)
                node.next = res
                res = node
            head = head.next


        return res
    

# solving with method 2 pointers
class Solution2:
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            Next = current.next
            current.next = prev
            prev = current
            current = Next

        return prev
    


# with recurtion
class Solution3:
    def reverseList(self, head):
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        
        head.next = None

        return newHead