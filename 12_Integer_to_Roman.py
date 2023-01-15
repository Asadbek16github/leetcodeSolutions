class Solution:
    def intToRoman(self, num: int) -> str:
        self.num = num

        a = num//1000
        b = (num//100)%10
        c = (num//10)%10
        d = num%10

        A = {0:"", 1:"M", 2:"MM", 3:"MMM"}
        B = {0:"", 1:"C", 2:"CC", 3:"CCC", 4:"CD", 5:"D", 6:"DC", 7:"DCC", 8:"DCCC", 9:"CM"}
        C = {0:"", 1:"X", 2:"XX", 3:"XXX", 4:"XL", 5:"L", 6:"LX", 7:"LXX", 8:"LXXX", 9:"XC"}
        D = {0:"", 1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX"}

        result = A[a]+B[b]+C[c]+D[d]
        return result
a = Solution()
print(a.intToRoman(1994))