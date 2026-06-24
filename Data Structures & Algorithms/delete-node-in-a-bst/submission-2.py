class Solution:        
    def findMinValue(self, root): 
        cur = root

        while cur and cur.left:
            cur = cur.left 
        
        return cur

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return None
        
        # search for the node to delete
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # find the node to delete

            # case 1 - the node has one child and 0 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # case 2 - the node has 2 childs
            else:
                minNode = self.findMinValue(root.right)
                # replace the root value with the minValue we just found
                root.val = minNode.val
                # recursively delete the duplicated value
                root.right = self.deleteNode(root.right, minNode.val)

        return root