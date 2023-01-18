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

a = Solution()
print(a.intersect(nums1 = [3,1,2], nums2 = [1,1]))