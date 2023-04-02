import math
class Solution:
    def successfulPairs(self, spells, potions, success):
        res = []
        potions.sort()
        def helperFunction(arr, num):
            l, r = 0, len(arr)-1
            while r>=l:
                mid = (l+r)//2
                if(arr[mid]>=num):
                    r = mid-1
                else:
                    l = mid+1
            return len(arr)-l if l<len(arr) else 0



        for i in range(len(spells)):
            q = math.ceil(success/spells[i])
            
            k = helperFunction(potions, q)
            res.append(k)
        return res