# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(6)
a.left = b
a.right = c
d = TreeNode(1)
e = TreeNode(3)
b.left = d
b.right = e

class Solution:
    def minDiffInBST(self, root):
        l = []

        def InOrderTraverse(tree):
            if tree:
                InOrderTraverse(tree.left)
                nonlocal l
                l.append(tree.val)
                InOrderTraverse(tree.right)
        
        InOrderTraverse(root)
        p, res = 1, float('inf')
        while p<len(l):
            res = min(res, l[p]-l[p-1])
            p+=1
        
        return res
    
print(Solution().minDiffInBST(a))

