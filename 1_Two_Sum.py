# my solution 
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

# Optimal Solution 

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        Checked_Numbers = {}
        i = 0
        while target-nums[i] not in Checked_Numbers:
            Checked_Numbers[nums[i]] = i
            i+=1
        
        return [Checked_Numbers[target-nums[i]], i]
