#  this is the first way 
class Solution:
    def addBinary(a: str, b: str) -> str:
        res = ''
        carry = 0
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            numA = int(a[i]) if i<len(a) else 0
            numB = int(b[i]) if i<len(b) else 0

            total = numA + numB + carry
            res = str(total%2) + res
            carry = total//2

        if carry:
            res = '1'+res
        
        return res


#  and this is the second
class Solution2:
    def addBinary(a, b):
        len_a = len(a)
        len_b = len(b)

        sum_a = 0
        sum_b = 0

        deg = 0
        while len_a or len_b:
            if(len_a):
                sum_a += int(a[len_a-1])*(2**deg)
                len_a -= 1
            
            if(len_b):
                sum_b +=int(b[len_b-1])*(2**deg)
                len_b-=1

            deg+=1
        
        total = sum_a+sum_b

        def recursiv(number):
            if(number<2):
                return str(number%2)

            else:
                return recursiv(number//2) + str(number%2)

        return recursiv(total)
            
print(Solution2.addBinary(a = "11", b = "1"))