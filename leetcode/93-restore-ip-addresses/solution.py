class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = []

        def backtrack(startIndex, segments):
            if len(segments) == 4:
                if startIndex == len(s):
                    output.append(".".join(segments))
                return

            for places in range(1,4):

                if startIndex + places > len(s):
                    break

                segment = s[startIndex:startIndex+places]

                if len(segment) > 1 and segment[0] == '0':
                    continue
                if int(segment) > 255:
                    continue


                backtrack(startIndex + places, segments + [segment])




        backtrack(0,[])
        return output