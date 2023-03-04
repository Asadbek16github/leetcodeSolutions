class Solution:
    def arthimeticTriplets(self, nums, diff):
        ans = 0
        memory = set()

        for i in nums:
            if i - diff in memory and i - 2*diff in memory:
                ans+=1
            
            memory.add(i)

        return ans
    
print(Solution().arthimeticTriplets(nums = [0,1,4,6,7,10], diff = 3))