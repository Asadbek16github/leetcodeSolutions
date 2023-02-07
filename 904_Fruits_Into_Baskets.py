class Solution:
    def totalFruit(fruits):
        basket = {}
        max_counter = 0
        left = 0

        for rigth in range(len(fruits)):
            basket[fruits[rigth]] = basket.get(fruits[rigth], 0) + 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if(basket[fruits[left]]==0):
                    del basket[fruits[left]]
                
                left+=1

            max_counter = max(max_counter, rigth-left+1)
        return max_counter


b = [0,1,2,2]
a = Solution
print(a.totalFruit(b))