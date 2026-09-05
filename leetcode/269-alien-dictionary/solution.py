class Solution:
    def alienOrder(self, words: List[str]) -> str:
        lettersAdjList = defaultdict(set)
        indegree = defaultdict(int)

        # Register every character
        for word in words:
            for ch in word:
                lettersAdjList[ch]
                indegree[ch] = 0

        # Compare adjacent words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            cur = 0
            minLength = min(len(word1), len(word2))

            while cur < minLength and word1[cur] == word2[cur]:
                cur += 1

            # Invalid ordering: ["abc", "ab"]
            if cur == minLength:
                if len(word1) > len(word2):
                    return ""
                continue

            a = word1[cur]
            b = word2[cur]

            if b not in lettersAdjList[a]:
                lettersAdjList[a].add(b)
                indegree[b] += 1

        queue = deque([])

        for letter in lettersAdjList:
            if indegree[letter] == 0:
                queue.append(letter)

        output = []

        while queue:
            letter = queue.popleft()
            output.append(letter)

            for nei in lettersAdjList[letter]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        for node in indegree:
            if indegree[node] != 0:
                return ""

        return "".join(output)