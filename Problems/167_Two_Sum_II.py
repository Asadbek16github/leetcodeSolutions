class Solution:
    def twoSum(numbers, target):
        left = 0
        rigth = len(numbers)-1

        while True:
            if(numbers[left]+numbers[rigth]==target):
                return [left+1, rigth+1]
            elif(numbers[left]+numbers[rigth]>target):
                rigth-=1
            else:
                left+=1

a = Solution
print(a.twoSum(numbers = [-1,0], target = -1))



