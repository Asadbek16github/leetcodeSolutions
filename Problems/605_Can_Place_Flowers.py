class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        
        b = True
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i]:
                b=False
            else:
                if b and flowerbed[i+1]==0:
                    n-=1
                    b = False
                else:
                    b=True
        return n<=0