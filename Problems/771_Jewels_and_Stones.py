class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a = set()
        counter = 0
        for i in jewels:
            if i not in a:
                counter+= stones.count(i)
                a.add(i)

        return counter