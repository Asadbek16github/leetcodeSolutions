class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while r>=l:
            mid = (r+l)//2
            hour = 0
            for i in piles:
                if i%mid==0:
                    hour+= i//mid 
                else:
                    hour+= i//mid + 1

            if hour<=h:
                r = mid-1
                k = mid

            else:
                l=mid+1

        return l


print(Solution().minEatingSpeed(piles = [3,6,7,11], h = 8))