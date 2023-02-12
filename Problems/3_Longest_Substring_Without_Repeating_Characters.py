
# My solution 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0): return 0

        res = 0
        l = 0                                         
        r = 1                                         
        myList = [letter for letter in s]             
        while len(myList)>=r:                         
            if(len(myList[l:r])==len(set(myList[l:r]))):
                res = max(res, r-l)
                r+=1
            else:
                l+=1
        return res


# This is better than mine

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])

            res = max(res, r-l+1)
        return res

