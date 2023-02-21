class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1 : return s
        
        res = ['' for i in range(numRows)]
        counter, d = 0, False
        
        for part in s:
            if counter == 0:
                res[counter] += part
                counter += 1
                d = not d
                
            elif counter < numRows-1:
                res[counter]+=part
                if d:
                    counter+=1
                else:
                    counter -=1
            
            elif counter == numRows-1:
                res[counter] += part
                counter -= 1
                d = not d
            
        ans = ''
        for i in res:
            ans+=i
            
        return ans

print(Solution().convert("PAYPALISHIRING", 3))