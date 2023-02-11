#  Birinchi yechim 

class Solution:
    def smallerNumbersThanCurrent(nums):
        N = len(nums)
        res = [0 for x in range(N)]
        
        for i in range(N):
            for j in range(i+1, N):
                if(nums[i]>nums[j]):
                    res[i] += 1
                elif(nums[i]<nums[j]):
                    res[j] +=1

        return res




#  ikkinchi yechim

class Solution2:
    def smallerNumbersThanCurrent(nums):
        
        numsDict = {}
        sortedList = sorted(nums)
        n = len(nums)
        res = []

        for i in range(n):
            if(sortedList[i] not in numsDict):
                numsDict[sortedList[i]]=i

        for j in nums:
            res.append(numsDict[j])
        
        return res