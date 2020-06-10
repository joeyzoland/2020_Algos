"""
https://leetcode.com/problems/find-common-characters/

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.



Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]


Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""

import copy
class Solution:
    def commonChars(self, A):
        #Create a character-frequency dictionary from the first word
        #Iterate through the remaining words, creating the same type of dictionary
            #Iterate through each of the keys in the first dictionary:
            #If there's a character match, retain the minimum
        #Iterate through the dictionary and output the relevant characters

        def freqDictConstructor(word):
            freqDict = {}
            for char in word:
                if char not in freqDict:
                    freqDict[char] = 1
                else:
                    freqDict[char] += 1
            return freqDict

        commonDict = freqDictConstructor(A[0])
        for word in A[1:]:
            currentDict = freqDictConstructor(word)
            tempDict = copy.deepcopy(commonDict)
            for char in commonDict:
                if char not in currentDict:
                    del tempDict[char]
                else:
                    tempDict[char] = min(commonDict[char], currentDict[char])
            commonDict = tempDict

        output = []
        for key in commonDict:
            while commonDict[key] > 0:
                output.append(key)
                commonDict[key] -= 1
        return output

solution = Solution()
input = ["bella","label","roller"]
print(solution.commonChars(input))
