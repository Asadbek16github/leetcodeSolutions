class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        self.nums = nums
        from math import fabs

        a = sum(nums)
        b = 0
        for x in nums:
            x = str(x)
            for y in x:
                b+=int(y)

        return int(fabs(a-b))

a = Solution()
print(a.differenceOfSum([1,15,6,3]))