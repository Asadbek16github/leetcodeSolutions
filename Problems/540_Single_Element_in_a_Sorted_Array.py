
#  The first solution
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1
        
        while l<r:
            mid = (l+r)//2
            
            if mid%2==0:
                if nums[mid] != nums[mid+1]:
                    r = mid
                
                elif nums[mid] == nums[mid+1]:
                    l = mid
                
            elif mid%2==1:
                if nums[mid] != nums[mid+1]:
                    l = mid+1
                    
                elif nums[mid] == nums[mid+1]:
                    r = mid-1
        return nums[l]
    


# the second solution 
class Solution2:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        return 2*sum(set(nums))-sum(nums)
    



# the third solution 
class Solution3:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1
        
        while l<r:
            mid = (l+r)//2
            
            if nums[mid]!=nums[mid+1]:
                if len(nums[mid+1:])%2==0:
                    r = mid
                elif len(nums[mid+1:])%2==1:
                    l = mid+1
                
            elif nums[mid]==nums[mid+1]:
                if len(nums[mid:])%2==1:
                    l = mid
                elif len(nums[mid:])%2==0:
                    r = mid-1
            
        return nums[l]