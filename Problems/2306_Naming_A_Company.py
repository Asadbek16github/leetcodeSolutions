import collections

class Solution:
    def distinctNames(ideas):
        letters = collections.defaultdict(set)
        for word in ideas:
            letters[word[0]].add(word[1:])
            
        result = 0
        for letter1 in letters:
            for letter2 in letters:
                if(letter1==letter2):
                    continue

                repieted_sufics = 0

                for sufics in letters[letter1]:
                    if(sufics in letters[letter2]):
                        repieted_sufics+=1
                
                distinct_suficss1 = len(letters[letter1])-repieted_sufics
                distinct_suficss2 = len(letters[letter2])-repieted_sufics

                result+=distinct_suficss1*distinct_suficss2

        return result




        
a = Solution
print(a.distinctNames( ideas = ['lack','back']))