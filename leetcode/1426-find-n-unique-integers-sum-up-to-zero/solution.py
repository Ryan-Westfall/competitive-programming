class Solution:
    '''
    if even
    [-1,1]
    [-1,-2,1,2]
    
    if odd:
    [-1,0,1]
    [-3,-2,-1,0,1,2,3]
    '''
    # def sumZero(self, n: int) -> List[int]:
    #     output = []
    #     for i in range(1, n//2 + 1):
    #         output += (-i,i)
    #     if n&1:
    #         output.append(0)
    #     return output
            
    '''
    A = [1,2,3,4,5]
    A.append(-sum(A))
    '''
    
    def sumZero(self, n: int) -> List[int]:
        output = list(range(1,n))
        output.append(-sum(output))
        return output