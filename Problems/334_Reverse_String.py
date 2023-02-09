class Solution:
    def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        rigth = len(s)-1

        while(rigth>left):
            s[left], s[rigth] = s[rigth], s[left]
            left+=1
            rigth-=1
        
        return s

a = Solution
print(a.reverseString(s = ["h","e","l","l","o"]))