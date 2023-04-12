class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = ''

        index = 0
        while index<len(path):
            pathWord = ''
            index+=1
            while index<len(path) and path[index]!='/':
                pathWord += path[index]
                index+=1
            if pathWord=='..':
                if len(stack):
                    stack.pop()
            elif pathWord != '' and pathWord!='.':
                stack.append(pathWord)

        return '/' + '/'.join(stack)