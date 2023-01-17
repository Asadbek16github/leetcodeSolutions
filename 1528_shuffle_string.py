class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        self.s = s
        self.indices = indices

        result = ''
        stringList = [letter for letter in s]
        for y in range(len(indices)):
            num = indices.index(y)
            result+=stringList[num]
            
        return result