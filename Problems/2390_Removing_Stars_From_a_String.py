class Solution:
    def removeStars(self, s: str) -> str:
        q = []
        for i in s:
            if i=="*":
                q.pop()
            else:
                q.append(i)

        return ''.join(q)