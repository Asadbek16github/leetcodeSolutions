class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        self.nums = nums
        self.target = target

        result = []
        n = 1
        for x in range(len(nums)):

            if result:
                break
            else:
                for y in range(n, len(nums)):
                    if(nums[x]+nums[y]==target):
                        result.append(x)
                        result.append(y)
                        break
            n+=1
        return result