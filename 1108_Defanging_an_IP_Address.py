class Solution:
    def defangIPaddr(self, address: str) -> str:
        self.address = address
        return address.replace('.', '[.]')

a = Solution()
print(a.defangIPaddr("1.1.1.1"))    