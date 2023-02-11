# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if(n<2):
            if(isBadVersion(n)==True):
                return n
        else:
            p = 1
            q = n
        
            while q>=p:
                mid = (p+q)//2
                if( isBadVersion(mid)==False and isBadVersion(mid+1)==False):
                    p=mid+1
                elif(isBadVersion(mid)==False and isBadVersion(mid+1)==True):
                    return (mid+1)
                elif(isBadVersion(mid)==True and isBadVersion(mid-1)==True):
                    q = mid-1
                elif(isBadVersion(mid)==True and isBadVersion(mid-1)==False):
                    return mid