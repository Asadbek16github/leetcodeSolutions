class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for x in range(n):
            result.append(nums[x])
            result.append(nums[x+n])
        
        return result