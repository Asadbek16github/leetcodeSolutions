class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowel = ['a', 'e', 'i', 'o', 'u']
        counter = 0
        for i in range(left, right+1):
            word = words[i]
            if (word[0] in vowel and word[-1] in vowel):
                counter+=1
                
        return counter
    

print(Solution().vowelStrings(words = ["are","amy","u"], left = 0, right = 2))