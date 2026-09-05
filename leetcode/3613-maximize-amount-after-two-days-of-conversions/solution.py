class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        # Helper function to build graph from pairs and rates
        def build_graph(pairs, rates):
            graph = {}
            for (src, dst), rate in zip(pairs, rates):
                if src not in graph:
                    graph[src] = {}
                if dst not in graph:
                    graph[dst] = {}
                graph[src][dst] = rate
                graph[dst][src] = 1.0 / rate
            return graph

        # Helper function to find all possible amounts using DFS
        def dfs(currency, amount, graph, visited):
            result = {currency: amount}
            visited.add(currency)
            
            for next_curr in graph.get(currency, {}):
                if next_curr not in visited:
                    next_amounts = dfs(next_curr, amount * graph[currency][next_curr], graph, visited)
                    for curr, amt in next_amounts.items():
                        if curr not in result or amt > result[curr]:
                            result[curr] = amt
            
            visited.remove(currency)
            return result

        # Build graphs for both days
        graph1 = build_graph(pairs1, rates1)
        graph2 = build_graph(pairs2, rates2)

        # Find all possible amounts after day 1
        day1_amounts = dfs(initialCurrency, 1.0, graph1, set())

        # Find maximum possible amount after day 2
        max_amount = 1.0

        # Try all intermediate currencies from day 1
        for curr, amount in day1_amounts.items():
            day2_amounts = dfs(curr, amount, graph2, set())
            if initialCurrency in day2_amounts:
                max_amount = max(max_amount, day2_amounts[initialCurrency])

        return max_amount