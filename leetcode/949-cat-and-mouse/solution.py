class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        from collections import deque

        n = len(graph)

        DRAW = 0
        MOUSE = 1
        CAT = 2

        # color[mouse][cat][turn]
        color = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]

        # number of moves available from each state
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        queue = deque()

        # initialize degrees
        for mouse in range(n):
            for cat in range(n):
                # mouse turn: mouse can move to any neighbor
                degree[mouse][cat][0] = len(graph[mouse])

                # cat turn: cat cannot move into the hole (0)
                degree[mouse][cat][1] = sum(1 for nei in graph[cat] if nei != 0)

        # terminal states
        for i in range(n):
            for turn in range(2):

                # mouse reaches hole
                color[0][i][turn] = MOUSE
                queue.append((0, i, turn, MOUSE))

                # cat catches mouse
                if i != 0:
                    color[i][i][turn] = CAT
                    queue.append((i, i, turn, CAT))

        def parents(mouse, cat, turn):
            """
            Find states that can move into (mouse, cat, turn)
            """

            result = []

            if turn == 0:
                # Current state is mouse's turn.
                # Previous turn was cat moving.
                # Cat moved from some previous node -> cat.
                for prev_cat in graph[cat]:
                    if prev_cat != 0:
                        result.append((mouse, prev_cat, 1))

            else:
                # Current state is cat's turn.
                # Previous turn was mouse moving.
                for prev_mouse in graph[mouse]:
                    result.append((prev_mouse, cat, 0))

            return result

        while queue:
            mouse, cat, turn, winner = queue.popleft()

            for pmouse, pcat, pturn in parents(mouse, cat, turn):

                # Already solved
                if color[pmouse][pcat][pturn] != DRAW:
                    continue

                # If previous player can make a move that wins immediately
                if pturn == 0 and winner == MOUSE:
                    # mouse's turn and mouse can move to mouse win
                    color[pmouse][pcat][pturn] = MOUSE
                    queue.append((pmouse, pcat, pturn, MOUSE))

                elif pturn == 1 and winner == CAT:
                    # cat's turn and cat can move to cat win
                    color[pmouse][pcat][pturn] = CAT
                    queue.append((pmouse, pcat, pturn, CAT))

                else:
                    # This move does not help previous player.
                    # Remove one possible move.
                    degree[pmouse][pcat][pturn] -= 1

                    # If no moves lead to a win, opponent wins
                    if degree[pmouse][pcat][pturn] == 0:
                        lose = CAT if pturn == 0 else MOUSE
                        color[pmouse][pcat][pturn] = lose
                        queue.append((pmouse, pcat, pturn, lose))

        return color[1][2][0]