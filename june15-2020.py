class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root != None:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left
        return None
