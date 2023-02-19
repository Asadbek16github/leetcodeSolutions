
# the first solution
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and not (n & n-1)
    

# the second solution
import math
class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and not math.log2(n)%1
    

# the third solution
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n.bit_count()==1
    
    

