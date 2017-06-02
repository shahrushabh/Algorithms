""" LEETCODE PROBLEMS """
import math

"""
    5. TOPTAL QUESTIONS
"""


"""
    4. NUMBER OF DIGIT ONE
"""


"""
    3. MEDIAN OF THE TWO SORTED ARRAYS
"""
# nums1 = [1, 2]
# nums2 = [3, 4]
# merged = []
# index1 = 0
# index2 = 0
#
# while(index1 <= len(nums1) or index2 <= len(nums2)):
#     if(index1 == len(nums1)):
#         while(index2 < len(nums2)):
#             merged.append(nums2[index2])
#             index2 += 1
#         break
#
#     if(index2 == len(nums2)):
#         while(index1 < len(nums1)):
#             merged.append(nums1[index1])
#             index1 += 1
#         break
#
#     if(nums1[index1] < nums2[index2]):
#         merged.append(nums1[index1])
#         index1 += 1
#     else:
#         merged.append(nums2[index2])
#         index2 += 1
#
# print(merged)
# indx = int(math.floor(len(merged)/2))
# if(len(merged) % 2 != 0):
#     print("Odd number of elements")
#     print(merged[indx])
# else:
#     print("Even number of elements")
#     median = (merged[indx-1] + merged[indx]) / 2.0
#     print(median)


"""
    2. LONGEST SUBSTRING WITHOUT REPLACING CHARACTERS
"""
# s = "abarushabhsmi"
#
# subString = ""
# lengthOfSubString = 0
#
# if(len(s) <= 1):
#     print(len(s))
# for index, char in enumerate(s):
#     for secondChar in s[index: len(s)]:
#         if(secondChar in subString):
#             if(len(subString) > lengthOfSubString):
#                 lengthOfSubString = len(subString)
#             subString = ""
#             break
#         else:
#             subString += secondChar
# print(lengthOfSubString)

"""
    1. TWO SUM PROBLEM.
"""
# nums = [1,5,11,4,23,30,25]
# target = 55
# indexes = []
# for index, value in enumerate(nums):
#     for secondIndex in range(index+1, len(nums)):
#         if(target == nums[index] + nums[secondIndex]):
#             indexes.append(index)
#             indexes.append(secondIndex)
#             print(indexes)
