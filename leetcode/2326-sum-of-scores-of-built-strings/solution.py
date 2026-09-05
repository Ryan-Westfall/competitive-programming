class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        
        # Choice of base and large prime modulo to minimize hash collisions
        p = 31
        m = 10**9 + 7
        
        # Precompute prefix hashes and powers of p
        h = [0] * (n + 1)
        power = [1] * (n + 1)
        
        for i in range(n):
            h[i + 1] = (h[i] * p + (ord(s[i]) - ord('a') + 1)) % m
            power[i + 1] = (power[i] * p) % m
            
        # Helper function to get the hash of substring s[L...R] inclusive
        def get_hash(L: int, R: int) -> int:
            res = (h[R + 1] - h[L] * power[R - L + 1]) % m
            return res if res >= 0 else res + m

        total_score = 0
        
        # Check every suffix starting at index i
        for i in range(n):
            low, high = 1, n - i
            lcp = 0
            
            while low <= high:
                mid = (low + high) // 2
                
                # Prefix hash: s[0 ... mid-1]
                prefix_hash = h[mid]
                # Suffix hash: s[i ... i+mid-1]
                suffix_hash = get_hash(i, i + mid - 1)
                
                if prefix_hash == suffix_hash:
                    lcp = mid      # Found a valid common prefix length
                    low = mid + 1  # Try to find a longer one
                    
                else:
                    high = mid - 1 # Try a shorter length
                    
            total_score += lcp
            
        return total_score