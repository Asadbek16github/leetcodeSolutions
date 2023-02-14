from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        self.nums1 = nums1
        self.nums2 = nums2
        nums3 = []

        for y in nums2:
            if(y in nums1):
                nums3.append(y)
                nums1.remove(y)
        return nums3


# This is realy realy realy faster solution
class Solution2:
    def intersect(self, nums1, nums2):
        a = Counter(nums1)
        res = []

        for i in nums2:
            if(a[i]>0):
                res.append(i)
                a[i]-=1
        return res

# The third solution
class Solution3:
    def intersect(self, nums1, nums2):

        nums1, nums2 = sorted(nums1), sorted(nums2)
        i, j = 0, 0
        res = []
         
        while i<len(nums1) and j<len(nums2):
            if(nums1[i]<nums2[j]):
                i+=1
            elif(nums1[i]>nums2[j]):
                j+=1
            else:
                res.append(nums1[i])
                i+=1
                j+=1
        return res



a = Solution3()
print(a.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))