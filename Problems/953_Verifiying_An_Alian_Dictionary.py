class Solution:
    def isAlienSorted(words, order):
        # dastur birinchi farq qiluvchi harfga qadar davom etadi
        # harflar bir hil bo'lib uzunliklari bilan farq qilsa uzuligi kichigi oldinda bo'ladi

        orderLetters = { letter : number for number, letter in enumerate(order)}

        for j in range(len(words)-1):
            word1, word2 = words[j], words[j+1]

            for i in range(len(word1)):
                if(i==len(word2)):
                    return False
                
                if(word1[i]!=word2[i]):
                    if(orderLetters[word2[i]]<orderLetters[word1[i]]):
                        return False
                    break
        return True

s = Solution
print(s.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))