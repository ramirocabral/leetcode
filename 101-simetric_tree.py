class Solution:
    def isSymetric(self, root : Optional[TreeNode]) -> bool:

        if not root:
            return False

        return self.isSymetricTree(root.left, root.right)

    # nodes inverted from #100
    def isSymetricTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p == None and q == None):
            return True
        
        if not (p and q):
            return False
        
        return self.isSameTree(p.left, q.right) and (q.val == p.val) and self.isSameTree(p.right, q.left)
