# Birinchi bo'lib uzimni yechimim keyingisida optimallroq yechim bo'ladi

class Solution:
    def moveZeroes(nums):

        for x in nums:
            if(x==0):
                nums.remove(x)
                nums.append(0)

        return nums

# a = Solution
# print(a.moveZeroes(nums = [0,1,0,3,12]))


class Solution2:
    def moveZeroes(nums):
        left = 0

        for rigth in range(len(nums)):
            if(nums[rigth]!=0):
                nums[left], nums[rigth] = nums[rigth], nums[left]
                left+=1

        return nums

a = Solution2
print(a.moveZeroes(nums = [0,1,0,3,12]))