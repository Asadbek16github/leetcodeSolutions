class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        l = 0
        while l+len(needle) <= len(haystack):
            if haystack[l:l+len(needle)]==needle:
                return l
            l+=1
        return -1


print(Solution().strStr(haystack = "sadbutsad", needle = "sad"))