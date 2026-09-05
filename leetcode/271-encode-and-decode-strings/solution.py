class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = ''
        for word in strs:
            output += chr(len(word)) + word

        return output

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        cur = 0
        prev = 0
        output = []
        while cur < len(s): 
            length = ord(s[cur])
            cur += 1 + length
            output.append(s[prev+1:cur])
            prev = cur

        return output

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))