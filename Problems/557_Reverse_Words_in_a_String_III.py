class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        
        for x in range(len(words)):
            words[x] = words[x][::-1]

        res = ''
        for x in range(len(words)):
            res+=words[x]
            if(x!=len(words)-1):
                res+=" "

        return res