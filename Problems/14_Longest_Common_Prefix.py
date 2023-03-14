# Aproach 1
class Solution:
    def longestCommonPrefix(self, strs):
        maxPrefix = ''

        for i in range(len(strs[0])):
            for j in strs:
                if i==len(j) or j[i]!=strs[0][i]:
                    return maxPrefix
            maxPrefix += strs[0][i]
            
        return maxPrefix
    

# Aproach 2
class Solution2:
    def longestCommonPrefix(self, strs):
        maxPrefix = strs[0]

        for i in strs:
            while i.find(maxPrefix) != 0:
                maxPrefix = maxPrefix[0: len(maxPrefix)-1]

        return maxPrefix