# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N"
        store = []
        stack = collections.deque([root])
        while stack:
            curr = stack.popleft()
            if not curr:
                store.append('N')
            else:
                store.append(str(curr.val))
                stack.append(curr.left)
                stack.append(curr.right)

        return ','.join(store)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        stack = collections.deque([root])
        index = 1
        while stack:
            curr = stack.popleft()
            if vals[index] != 'N':
                curr.left = TreeNode(int(vals[index]))
                stack.append(curr.left)
            index += 1
            if vals[index] != 'N':
                curr.right = TreeNode(int(vals[index]))
                stack.append(curr.right)
            index += 1

        return root
            
                


        return data
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))