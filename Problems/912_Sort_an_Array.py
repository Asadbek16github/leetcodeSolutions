
from random import randrange
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def QuickSort(arr):
            if len(arr)<2 or len(set(arr))<2:
                return arr
            else:
                pivot = arr.pop(randrange(len(arr)))
                lowers = [i for i in arr if i<=pivot ]
                uppers = [i for i in arr if i>pivot]
                return QuickSort(lowers) + [pivot] + QuickSort(uppers)

        return QuickSort(nums)
    
print(Solution().sortArray([3,2,1,5,32,5,23,7]))