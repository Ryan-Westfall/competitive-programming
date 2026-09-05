class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adjacencyMap = defaultdict(list)

        # Build graph
        for word in wordList:
            for i in range(len(word)):
                pWord = word[:i] + "*" + word[i+1:]
                adjacencyMap[pWord].append(word)

        
        queue = collections.deque([(beginWord, 1)])
        visited = set()

        # Traverse graph, use bfs since we are finding shortest path
        while queue:
            word, distance = queue.popleft()

            if word == endWord:
                return distance

            visited.add(word)

            for i in range(len(word)):
                pWord = word[:i] + "*" + word[i+1:]

                for newWord in adjacencyMap[pWord]:
                        if newWord not in visited:
                            queue.append((newWord, distance + 1))

                # pWords = adjacencyMap.get(pWord, None)

                # if pWords:
                #     for newWord in pWords:
                #         if newWord not in visited:
                #             queue.append((newWord, distance + 1))

        return 0


            




