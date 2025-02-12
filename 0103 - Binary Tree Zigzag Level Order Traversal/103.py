# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution A:
#   use a queue. We will iterate through the tree one row at a time (BFS), while adding all children to the queue
#   before moving to the next row, we will build a list of values to add to the answer
#   we will keep track of which direction the row must be added in

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        answer = []
        q = deque([root])

        direction = 1
        while(len(q) > 0):
            row = []
            # complete one full row, while adding all child elements to the queue
            for _ in range(0, len(q)):
                current = q.popleft()
                row.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            
            # this is an expensive operation, can it be optimized away? maybe by appending in the correct direction right away
            answer.append(row[::direction])
            direction *= -1

        return answer




if __name__ == '__main__':
    s = Solution()