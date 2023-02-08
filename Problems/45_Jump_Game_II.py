class Solution:
    def jump(nums):
        step_counter = 0
        left = 0
        rigth = 0

        while(rigth < len(nums)-1):
            far_distance = 0
            for x in range(left, rigth+1):
                far_distance = max(far_distance, x+nums[x])

            left = rigth+1
            rigth = far_distance
            step_counter +=1
        
        return step_counter

a = Solution
print(a.jump([2,3,1,1,4]))