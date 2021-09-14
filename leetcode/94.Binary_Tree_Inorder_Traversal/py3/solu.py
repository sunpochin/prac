# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)

from typing import Optional, List

class Solution:
    thelist = []

    def traverse(self, node: Optional[TreeNode]):
        if None == node:
            return []
        
        if None != node.left:
            self.traverse(node.left)

        if None == node:
            return
        self.thelist.append(node.val)
            
        if None != node.right:
            self.traverse(node.right)
        
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.thelist = []
        self.traverse(root)
        print(self.thelist)
        return self.thelist

head = TreeNode(val=3)
head = TreeNode(val=2, left=head)
head = TreeNode(val=1, right=head)

# inp = [1,None,2,3]
sol = Solution()
ret = sol.inorderTraversal(head)
print('ret: ', ret)
