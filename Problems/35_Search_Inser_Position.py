class Solution:
    def searchInsert(nums, target):
        l, r = 0, len(nums)-1

        while r >= l:
            mid = (l+r)//2
            if(nums[mid]==target):
                return mid                
            elif(nums[mid]>target):
                r= mid-1
            else:
                l= mid+1
        return l