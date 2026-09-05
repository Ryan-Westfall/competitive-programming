class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        total = len(arr)
        i = 0
        while i < len(arr):
            if i == total:
                break;
            if arr[i] == 0:
                arr.insert(i+1,0)
                i+=1
                arr.pop()
            i+=1
        