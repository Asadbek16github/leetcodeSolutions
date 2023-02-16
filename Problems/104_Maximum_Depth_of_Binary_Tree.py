# The first way is solve with recurtion
class Solution:
    def maxDepth(self, root) -> int:
        if not root: return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    



# The second way is solve this problem with BFS
from collections import deque
class Solution2:
    def maxDepth(self, root) -> int:
        if not root: return 0

        D = deque()
        D.append(root)
        step = 0
        while D:
            n = len(D)
            for i in range(n):
                val = D.popleft()
                if val.left:
                    D.append(val.left)
                if val.right:
                    D.append(val.right)
            step+=1

        return step
    



# The third way is DFS algorith

class Solution:
    def maxDepth(self, root) -> int:
        stack = [[root, 1]]
        step = 0

        while stack:
            root_val, step_val = stack.pop()
            if root_val:
                step = max(step, step_val)
                stack.append([root_val.right, step_val+1])
                stack.append([root_val.left, step_val+1])
        return step