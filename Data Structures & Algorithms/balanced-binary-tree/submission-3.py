class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # return [first-value: is this a balanced tree or not, second-value: height of the subtree]
        def dfs(root):
            if not root:
                return [True, 0]
            
            # from the left subtree, and right subtree are they balanced?
            left, right = dfs(root.left), dfs(root.right)

            # from the root node is that balance
            is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [is_balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]