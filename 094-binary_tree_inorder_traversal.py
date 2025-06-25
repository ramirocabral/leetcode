class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []

        self.traverse(root, list)

        return list

    def traverse(self, root: Optional[TreeNode], list : List[int]):
        if root == None:
            return

        self.traverse(root.left, list)
        list.append(root.val)
        self.traverse(root.right,list)
