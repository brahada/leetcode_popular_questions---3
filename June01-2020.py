class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root:
            # General case:
            
            # invert child node of current root
            root.left, root.right = root.right, root.left
            
            # invert subtree with DFS
            
            if root.left:
                self.invertTree( root.left )
            
            if root.right:
                self.invertTree( root.right )
            
            return root
        
        else:
            # Base case:
            return None



#alternate 3-lines solution
'''
def invert(self,root):
    if not root: return None
    root.left,root.right=self.invert(root.right),self.invert(root.left)
    return root

'''
