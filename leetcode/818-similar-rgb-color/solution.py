class Solution:
    def similarRGB(self, color: str) -> str:
        color = color.strip('#')

        output = ['#']

        for i in range(0, 6, 2):
            x = int(color[i:i+2], 16)
            digit = (x + 8) // 17
            output.append(f"{digit:x}" * 2)

        return "".join(output)