# # Example 1
# # Input: nums = [1,2,3]
# # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

def subsets(nums):
    len_nums = len(nums)
    result = []
    solution = []

    def backtrack(index):
        if index >= len_nums:
            result.append(solution[:])
            return
        
        # if dont pick the number
        backtrack(index + 1)

        # if the number is picked
        solution.append(nums[index])
        backtrack(index + 1)
        solution.pop()

    backtrack(0)
    return result

if __name__ == '__main__':
    values = [1,2,3]
    print(subsets(values))


# Example 2
# Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def subsets(nums):
    len_nums = len(nums)
    res , sol = [] , []

    def backtrack():
        if len(sol) == len_nums:
            res.append(sol.copy())
            return
        
        for val in nums:
            if val not in sol:
                sol.append(val)
                backtrack()
                sol.pop()
    
    backtrack()
    return res

if __name__ == '__main__':
    values = [1,2,3]
    print(subsets(values))


# Example 3 
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

def combine(n,k):
    res , sol = [] , []

    def backtrack(x,k):
        if len(sol) == k:
            res.append(sol[:])
            return
        
        left = x
        still_need = k - len(sol)

        if left > still_need:
            backtrack( x - 1 )

        sol.append(x)
        backtrack( x - 1)
        sol.pop()

    backtrack(n)
    return res

if __name__ == '__main__':
    values = [1,2,3]
    print(combine(4,2))


