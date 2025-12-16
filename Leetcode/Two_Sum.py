'''
No.1 two sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]
    return []

print(two_sum([2, 7, 11, 15], 9))



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
        return []

'''
No. 2239 Find Closest Number to Zero

Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

'''

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        for i in rnage(len(nums)):
            distance = abs(nums[i])

            if distance < closest_distance:
                
                closest_distance = distance
                closest_number = nums[i]

        return closest_number

print(Solution().findClosestNumber([-4, -2, 1, 4, 8]))

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_number = nums[0]
        closest_distance = abs(nums[0])

        for i in range(1, len(nums)):
            distance = abs(nums[i])

            # Smaller distance is better
            # If equal distance, pick the larger value (e.g., 2 beats -2)
            if distance < closest_distance or (distance == closest_distance and nums[i] > closest_number):
                closest_distance = distance
                closest_number = nums[i]

        return closest_number

'''
No. 1768 Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = []
        len1 = len(word1)
        len2 = len(word2)
        min_len = min(len1, len2)

        for i in range(min_len):
            merged_string.append(word1[i])
            merged_string.append(word2[i])

        if len1 > len2:
            merged_string.extend(word1[min_len:])
        else:
            merged_string.extend(word2[min_len:])

        return "".join(merged_string)

print(Solution().mergeAlternately("abc", "pqr"))