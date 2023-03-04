class Solution:
    def splitNum(self, num: int) -> int:
        d = []
        for i in range(len(str(num))):
            k = num%10
            num = num//10
            d.append(k)
        d.sort()
        num1 = ''
        num2 = ''
        for j in range(len(d)):
            if(j%2==1):
                num1+=str(d[j])
            else:
                num2+=str(d[j])

        return int(num1) + int(num2)