# Solution 1
class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        num = num[::-1]
        len_k = len(str(k))
        len_num = len(num)

        carry = 0
        for i in range(max(len_k, len_num)):
            if i>len_k-1:
                val_1=0
            else:
                val_1=k%10
                k //=10

            if i>len_num-1:
                val_2=0
            else:
                val_2=num[i]

            s = carry + val_1 + val_2
            if(len_num-1>=i):
                num[i]=s%10
            else:
                num.append(s%10)
            carry = s//10
        if carry:
            num.append(carry)

        return num[::-1]
    

# Solution 2
class Solution2:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i = 0
        num = num[::-1]

        while k:
            digit = k%10
            if(i<len(num)):
                num[i]+=digit
            else:
                num.append(digit)

            carry = num[i]//10
            num[i] = num[i] % 10

            k //=10
            k +=carry
            i+=1
        
        return num[::-1]