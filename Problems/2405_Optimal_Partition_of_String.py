class Solution:
    def partitionString(self, s):
        m = set()
        counter = 0

        for i in s:
            if i in m:
                counter+=1
                m = set()
            m.add(i)

        return counter+1

print(Solution().partitionString('abacda'))