# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        
        D = deque()
        res = []
        res.append([root.val])
        D.append(root)
        while D:
            n = len(D)
            res1 = []
            for i in range(n):
                ROOT = D.popleft()
                if ROOT.left:
                    res1.append(ROOT.left.val)
                    D.append(ROOT.left)
                
                if ROOT.right:
                    res1.append(ROOT.right.val)
                    D.append(ROOT.right)

            if len(res1):
                res1 = reversed(res1) if(len(res)%2==1) else res1
                res.append(res1)

        return res
