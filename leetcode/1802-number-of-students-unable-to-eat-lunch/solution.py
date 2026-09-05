class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        countStudents = Counter(students)
        res = len(students)

        for s in sandwiches:
            if countStudents[s] > 0:
                countStudents[s] -= 1
                res -= 1
            else:
                return res

        return res



        
        