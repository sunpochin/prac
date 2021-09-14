# recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def ismirror(self, nodeA, nodeB) -> bool:
        if None == nodeA and None == nodeB:
            return True
        if None == nodeA or None == nodeB:
            return False
        return  nodeA.val == nodeB.val and \
                self.ismirror(nodeA.left, nodeB.right) and \
                self.ismirror(nodeA.right, nodeB.left)
        
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ret = self.ismirror(root, root)
        return ret


# iteratively.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def nlr(node, res):
            if None == node:
                res.append(0)
                return
            res.append(node.val)
            nlr(node.left, res)
            nlr(node.right, res)
            
        def nrl(node, res):
            if None == node:
                res.append(0)
                return
            res.append(node.val)
            nrl(node.right, res)
            nrl(node.left, res)
            
        def ismirror(left, right):
            leftres = []
            rightres = []
            nlr(left, leftres)
            nrl(right, rightres)
            # print('leftres: ', leftres, ', rightres: ', rightres)
            return leftres == rightres
        result = ismirror(root.left, root.right)
        return result