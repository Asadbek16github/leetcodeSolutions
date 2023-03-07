# Aproach 1

class Solution:
    def removeOuterParentheses(self, s):
        res, Open, skip = [], 0, True

        for i in range(len(s)):
            if skip:
                skip = False
                continue

            elif s[i] == '(':
                Open+=1
                res.append('(')

            elif not Open:
                skip = True

            else:
                Open-=1
                res.append(')')
                
        return "".join(res)
            


# Aproach 2
class Solution2:
    def removeOuterParentheses(self, s):
        res = []
        l, q = 0, 0
        for r in range(len(s)+1):
            if q == 0 and r!=0 :
                res.append(s[l+1:r-1])
                l = r
                if r == len(s):
                    break
            if s[r]=='(':
                q+=1
            elif s[r]==')':
                q-=1

        return "".join(res)
            

print(Solution2().removeOuterParentheses(s = "(()())(())"))