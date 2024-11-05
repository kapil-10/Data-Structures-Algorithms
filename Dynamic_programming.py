# F(0) = 0
# F(1) = 1
    
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# # 1 - Top Down Recursive  , Time: O(2^n) ,  Space: O(n)

def top_down_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return top_down_recursive(n-1) + top_down_recursive(n-2)

# 2 - # Top Down Memoized , Time: O(n) , Space: O(n)

def top_down_memoization(n):
    memo = {0:0, 1:1}

    if n in memo:
        return memo[n]
    else:
        memo[n] = top_down_memoization(n-2) + top_down_memoization(n-1)
        return memo[n]
    
# 3 - Bottom up Tabulation  , Time: O(n) , Space: O(n)

def bottom_up_tabulation(n):
    table = [0] * (n + 1)

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    table[0] = 0
    table[1] = 1

    for value in range(2,n+1):
        table[value] = table[value - 1] + table[value - 2]

    return table[n]


# 4 - bottom up constant time , Time: O(n) , Space: O(1)

def bottom_up_constant_time(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    prev = 0
    curr = 1

    for value in range(2,n+1):
        prev , curr = curr , prev + curr

    return curr


if __name__ == '__main__':

    print('Top-down-recursive :',top_down_recursive(10))
    print('Top-Down-Memoization :',top_down_memoization(10))
    print('Bottom-up-tabulization',bottom_up_tabulation(10))
    print('Bottom-up-constant-time :',bottom_up_constant_time(10))