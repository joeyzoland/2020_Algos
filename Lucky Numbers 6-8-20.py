"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.



Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]


Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
"""

class Solution:
    def luckyNumbers (self, matrix):
        #Initialize output
        #For each row
            #Find the minimum in a row
                #If all numbers are smaller than it in its column, add to output
        #Return output
        output = []
        row_length = len(matrix[0])
        column_length = len(matrix)
        for r in matrix:
            min_index = 0
            min_val = r[0]
            for i in range(1, row_length):
                if r[i] < min_val:
                    min_index = i
                    min_val = r[i]
            max_bool = True
            for c in range(column_length):
                if matrix[c][min_index] > min_val:
                    max_bool = False
                    break
            if max_bool:
                output.append(min_val)
        return output

solution = Solution()
matrix = [[3,7,8],[9,11,13],[15,16,17]]
print (solution.luckyNumbers(matrix))
