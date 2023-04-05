class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        counter = 0
        l, r = 0, len(people)-1

        while r>=l:
            if people[r]+people[l]<=limit:
                l+=1
            counter+=1
            r-=1
        return counter

print(Solution().numRescueBoats(people = [1,2], limit = 3))