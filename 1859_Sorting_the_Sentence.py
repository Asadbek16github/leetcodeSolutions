class Solution:
    def sortSentence(self, s: str) -> str:
        word_list = s.split()
        dic = {}
        result = ''
        for string in word_list:
            dic[int(string[-1])]=string[:-1]
        
        for x in range(len(word_list)):
            result+=dic[x+1]
            if(x!=len(word_list)-1):
                result+=" "

        return result