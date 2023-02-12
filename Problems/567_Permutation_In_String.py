class Solution:
    def checkInclusion(s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)): return False

        else:
            dicS1, dicS2 = {}, {}

            for x in range(len(s1)):
                dicS1[s1[x]] = dicS1.get(s1[x], 0)+1
                dicS2[s2[x]] = dicS2.get(s2[x], 0)+1

            if(dicS1==dicS2): return True

            l = 0
            for r in range(len(s1), len(s2)):
                dicS2[s2[l]]-=1
                if(dicS2[s2[l]]==0): del dicS2[s2[l]]
                l+=1
                dicS2[s2[r]] = dicS2.get(s2[r], 0) + 1

                if(dicS1==dicS2): return True

            return False

print(Solution.checkInclusion(s1 = "adc", s2 = "dcda"))