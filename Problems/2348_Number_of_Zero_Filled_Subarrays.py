class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        res, counter = 0, 0
        for i in nums:
            if i==0:
                counter+=1
            else:
                if counter!=0:
                    res+=(1+counter)*counter//2
                    counter=0
        if counter!=0:
            res+=(1+counter)*counter//2

        return res