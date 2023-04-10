class Solution:
    def isValid(self, s: str) -> bool:
        dic = { '}': '{', ')':'(', ']':'[' }
        stack = []

        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                else:
                    q = stack.pop()
                    if q!=dic[i]:
                        return False
        return True if len(stack)==0 else False