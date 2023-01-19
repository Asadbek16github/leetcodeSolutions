class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        self.nums = nums

        pointer = 0
        result = []
        for x in nums:
            result.append(x+pointer)
            pointer+=x
        return result

p = Solution()
print(p.runningSum([1,1,1,1,1]))