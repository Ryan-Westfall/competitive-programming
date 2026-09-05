class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        last_start = 0
        output = [0] * n
        for log in logs:
            ID_str, signal, time_str = log.split(":")
            ID, time = int(ID_str), int(time_str)
            if signal == "start":
                if stack:
                    output[stack[-1]] += time - last_start

                stack.append(ID)
                last_start = time
            else:
                output[stack.pop()] += time - last_start + 1
                last_start = time + 1


        return output
            
