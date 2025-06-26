class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p == None and q == None):
            return True
        
        if not (p and q):
            return False
        
        return self.isSameTree(p.left, q.left) and (q.val == p.val) and self.isSameTree(p.right, q.right)
