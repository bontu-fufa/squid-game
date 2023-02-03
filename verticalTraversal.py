# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        res = collections.defaultdict(list)
        
        queue = deque()
        queue.append((0,0,root))
        
        while queue:
            row,col,node = queue.popleft()
            res[col].append((row,node.val))
            if node.left: 
                queue.append((row+1, col-1, node.left))
            if node.right: 
                queue.append((row+1, col+1, node.right))

        res_values = []
        for col in sorted(res.keys()):
            res_values.append(val for _, val in sorted(res[col]))
        return res_values
