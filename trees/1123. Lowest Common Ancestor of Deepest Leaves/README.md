## Problem

https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description

Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

## Solution
We can solve this problem recursively as follows:
- If the root is a leaf, it obviously has to be the solution.
- If both the left and right subtrees of the root contain a deepest leaf, the root also has to be the solution, since neither subtree can contain all the deepest leaves.
- Otherwise we repeat this process on whichever subtree contains a deepest leaf.

So how can we efficiently know which subtree(s) contain a deepest leaf?

We can preprocess the tree and compute the depth of each node, defined recursively as 1 if the node is a leaf and 1 + the maximum depth of all its subtrees otherwise. Then we know whichever subtree has the maximum depth must contain a deepest leaf.

This comes out to a two-pass algorithm in $O(n)$.

## Code
```
class Solution:
    def setDepth(self, root):
        if not root:
            return 0
        leftDepth = self.setDepth(root.left)
        rightDepth = self.setDepth(root.right)
        rootDepth = max(leftDepth, rightDepth) + 1
        root.depth = rootDepth
        return rootDepth

    def getLCA(self, root):
        leftDepth = 0 if not root.left else root.left.depth
        rightDepth = 0 if not root.right else root.right.depth
        if leftDepth == rightDepth:
            return root
        if leftDepth < rightDepth:
            return self.getLCA(root.right)
        if leftDepth > rightDepth:
            return self.getLCA(root.left)        

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.setDepth(root)
        return self.getLCA(root)
```