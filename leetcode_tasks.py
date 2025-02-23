"""
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)


        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10

        reversed_x *= sign

        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x
"""



""" 3Sum
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, n = [], len(nums)
        for i in range(n-2):
            if i and nums[i]==nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
"""
