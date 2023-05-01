# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.


class Solution:
    def average(self, salary: List[int]) -> float:
        mini = salary[0]
        maxi = salary[0]
        total = 0

        for i in salary[1:]:
            if i < mini:
                if mini != maxi:
                    total += mini
                mini = i
            elif i > maxi:
                if mini != maxi:
                    total += maxi
                maxi = i
            else:
                total += i
        
        return total / (len(salary) - 2)
