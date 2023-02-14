# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





# The first way is create new binary tree and add sum of root1 and root2
class Solution:
    def mergeTrees(self, root1, root2):
        if not root1 and not root2:
            return None

        value_1 = root1.val if root1 else 0
        value_2 = root2.val if root2 else 0

        new_root = TreeNode(value_1+value_2)

        new_root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else 0)
        new_root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)


        return new_root



# The second way is just modify root1
class Solution2:
    def mergeTrees(self, root1, root2):
        if(root1 == None):
            return root2
        if(root2 == None):
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1