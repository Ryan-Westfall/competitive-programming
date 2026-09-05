class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        numbers = []
        freq = {}
        for item in arr:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        for i in freq.values():
            numbers.append(i)
        numbers.sort();
        total = 0
        count = 0
        for i in range(len(numbers),0,-1):
            count += numbers[i-1] 
            total += 1
            if count >= len(arr)/2:
                return total 
