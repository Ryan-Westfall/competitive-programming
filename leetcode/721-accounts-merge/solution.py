class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graphAdjList = collections.defaultdict(set)
        emailToName = {}

        for account in accounts:
            name = account[0]

            for email in account[1:]:
                graphAdjList[account[1]].add(email)
                graphAdjList[email].add(account[1])
                emailToName[email] = name



        res = []
        seen = set()
        for email in graphAdjList:
            if email not in seen:
                stack = [email]
                seen.add(email)
                local = []

                while stack:
                    node = stack.pop()

                    local.append(node)
                    for edge in graphAdjList[node]:
                        if edge not in seen:
                            stack.append(edge)
                            seen.add(edge)

                res.append([emailToName[email]] + sorted(local))

        return res





