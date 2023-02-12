class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        self.nums = nums

        s = set()
        for x in nums:
            if(x in s):
                return True
            else:
                s.add(x)
        
        return False