import math

class Solution:
    def minimizeArrayValue(self, nums):
        maxVal = total = nums[0]

        for i in range(1, len(nums)):
            total = total + nums[i]
            maxVal = max(maxVal, math.ceil(total / (i+1)))

        return maxVal
    
print(Solution().minimizeArrayValue(nums = [3,7,1,6]))