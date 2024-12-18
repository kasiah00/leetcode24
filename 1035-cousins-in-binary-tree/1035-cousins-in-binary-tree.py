# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return None
        queue = deque([(root, None)])
        found = 0
        last_parent = None

        while queue:
            for _ in range(len(queue)):
                node, parent = queue.popleft()
                if found == 1 and node.val in (x, y) and parent != last_parent:
                    return True
                elif found == 1 and node.val in (x, y) and parent == last_parent:
                    return False
                elif node.val in (x, y):
                    found += 1
                    last_parent = parent
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            if found == 1:
                return False