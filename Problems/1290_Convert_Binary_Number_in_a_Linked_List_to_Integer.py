# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Aproach 1
class Solution:
    def getDecimalValue(self, head):
        s = ''

        while head:
            s = str(head.val) + s
            head = head.next

        ans = 0        
        for i in range(len(s)):
            ans+=(pow(2,i))*int(s[i])

        return ans
    


# Aproach 2
class Solution:
    def getDecimalValue(self, head):
        s = ''

        while head:
            s = s+str(head.val)
            head = head.next

        return int(s, 2)


