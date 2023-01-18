class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.nums = nums

        a = len(nums)
        for x in range(a):
            for y in range(a):
                if(nums[x]<nums[y]):
                    temp = nums[x]
                    nums[x] = nums[y]
                    nums[y] = temp