class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(a, b):
            if b == 0:
                return a

            return gcd(b, a%b)

        a = len(str1)
        b = len(str2)
        if b > a:
            a,b = b,a

        possible = gcd(a, b)

        return str1[:possible]


        