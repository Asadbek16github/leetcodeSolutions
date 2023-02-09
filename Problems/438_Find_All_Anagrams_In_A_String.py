class Solution:
    def findAnagrams(s, p):
        if len(p)> len(s):
            return []

        sdict, pdict = {}, {}
        for i in range(len(p)):
            pdict[p[i]] = pdict.get(p[i], 0) + 1
            sdict[s[i]] = sdict.get(s[i], 0) + 1

        res = [0] if sdict == pdict else []

        left = 0
        for rigth in range(len(p), len(s)):
            sdict[s[left]]-=1
            if(sdict[s[left]]==0):
                del sdict[s[left]]
            
            left+=1
            sdict[s[rigth]] = sdict.get(s[rigth], 0) + 1

            if sdict==pdict:
                res.append(left)

        return res

A = Solution
print(A.findAnagrams(s = "cbaebabacd", p = "abc"))