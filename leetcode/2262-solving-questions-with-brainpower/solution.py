class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        @cache
        def dp(i):
            if i >= n:
                return 0


            noTake = dp(i+1)
            point, brainpower = questions[i]
            take = dp(i+brainpower+1) + point

            return max(take, noTake)

        return dp(0)
