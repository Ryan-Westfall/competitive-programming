from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op not in {"C", "D", "+"}:
                stack.append(int(op))
            elif op == 'C' and stack:
                stack.pop()
            elif op == 'D' and stack:
                stack.append(stack[-1] * 2)
            elif op == '+' and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])

        # Return the sum of the scores
        return sum(stack)
