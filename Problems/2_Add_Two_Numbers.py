# my solution

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []

        start_1 = l1
        start_2 = l2
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        if(len(s1)>len(s2)):
            a = len(s1)-len(s2)
            while a:
                s2.append(0)
                a-=1
        elif(len(s1)<len(s2)):
            a = len(s2)-len(s1)
            while a:
                s1.append(0)
                a-=1

        coun = 0
        head = ListNode(0)
        last = head
        for i in range(0, len(s1)):
            if(i==0):
                s = s1[i]+s2[i]
                s, coun = s%10, s//10
                head.val = s
            else:
                s = s1[i]+s2[i]+coun
                s, coun = s%10, s//10
                last.next = ListNode(s)
                last = last.next
        if(coun==1):
            last.next = ListNode(1)

        return head


# this is a little bit faster than mine

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prevHead = ListNode(0)
        currentNode = prevHead
        sum_two_val = 0

        while l1 or l2 or sum_two_val:
            if l1:
                sum_two_val+=l1.val
                l1 = l1.next
            if l2:
                sum_two_val+=l2.val
                l2 = l2.next

            currentNode.next = ListNode(sum_two_val%10)
            currentNode = currentNode.next
            sum_two_val = sum_two_val//10
        return prevHead.next