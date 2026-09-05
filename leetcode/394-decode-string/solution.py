class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        index = 0

        while index < len(s):
            char = s[index]
            if char != ']':
                stack.append(char)
            else:
                substring = ''
                while stack and stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()

                multiplier = ''
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                stack.append(int(multiplier) * substring)

            index += 1
        
        return "".join(stack)
        