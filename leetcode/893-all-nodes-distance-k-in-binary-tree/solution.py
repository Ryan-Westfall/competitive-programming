# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Create adjacency list
        adj = defaultdict(list)

        def dfs(node):
            if not node:
                return

            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)           

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        # bfs from target over adjacency list
        q = collections.deque([target.val])
        distanceFromTarget = 0
        res = []
        visited = set([target.val])  # Use "visited" to track already processed nodes
        while q:
        # Process all nodes at the current level
            for _ in range(len(q)):
                cur = q.popleft()
                
                # If we've reached the target distance, collect the result
                if distanceFromTarget == k:
                    res.append(cur)

                # Enqueue all unvisited neighbors
                for neighbor in adj[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)

            # Move to the next level
            distanceFromTarget += 1

            # Exit early if we've found all nodes at distance k
            if distanceFromTarget > k:
                break

        return res
            
            


        