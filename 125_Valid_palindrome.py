class Solution:
    def isPalindrome(self, s: str) -> bool:
        self.s = s
        myWord = ""
        for x in s:
            if(x.isalnum()):
                myWord+=x.casefold()
        if(myWord == myWord[::-1]):
            return True
        else:
            return False

a = Solution()        
print(a.isPalindrome("A man, a plan, a canal: Panama"))