class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        output = 0
        curSum = 0
        l = 0
        
        for r in range(len(arr)):
            curSum += arr[r]  # 1. Expand the window to include arr[r]
            
            # 2. Once the window size hits k:
            if (r - l + 1) == k:
                # Check average (or compare sum directly to avoid division: curSum >= threshold * k)
                if curSum / k >= threshold:
                    output += 1
                
                # 3. Slide the left boundary rightward to prepare for next step
                curSum -= arr[l]
                l += 1

        return output