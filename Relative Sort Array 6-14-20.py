"""
https://leetcode.com/problems/relative-sort-array/

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.



Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]


Constraints:

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.
"""

class Solution:
    def relativeSortArray(self, arr1, arr2):
        #Make a dictionary, mapping numbers onto indices, and a corresponding array
        #Initialize an array that holds all of array 1 not in in array 2
        #Iterate through array 1, sorting into the two aforementioned arrays
        #Iterate through frequency array, adding to solution array
        #Sort all of the remaining array, then add it onto solution array
        freqArr = [0] * len(arr2)
        freqArrMap = {}
        remainingArr = []
        output = []
        for i in range(len(arr2)):
            freqArrMap[arr2[i]] = i
        for num in arr1:
            if num in freqArrMap:
                freqArr[freqArrMap[num]] += 1
            else:
                remainingArr.append(num)
        for i in range(len(freqArr)):
            for n in range(freqArr[i]):
                output.append(arr2[i])
        remainingArr.sort()
        output = output + remainingArr
        return output

solution = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(solution.relativeSortArray(arr1, arr2))
