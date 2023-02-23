class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        addingNum = 1
        l = len(digits)
        
        while l and addingNum:
            val = digits[l-1]+addingNum
            addingNum = val//10
            digits[l-1] = val%10 if val>0 else  0
            l-=1
            
        if addingNum:
            digits.insert(0, addingNum)
            
        return digits
    

print(Solution().plusOne([9,9,9,9]))
print(Solution().plusOne([1,2,3]))