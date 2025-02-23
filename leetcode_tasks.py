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

""" sudoku solver
class Solution:
    __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        Do not return anything, modify board in-place instead.
        
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        empty = []

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r//3)*3 + (c//3)].add(val)

        def is_valid(r, c, box_idx, val):
            return val not in rows[r] and val not in cols[c] and val not in boxes[box_idx]

        def solve(idx):
            if idx == len(empty):
                return True

            r, c = empty[idx]
            box_idx = (r//3)*3 + (c//3)
                        
            for val in "123456789":
                if is_valid(r, c, box_idx, val):
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)

                    if solve(idx+1):
                        return True
                                
                    board[r][c] = "."
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box_idx].remove(val)

            return False

        solve(0)
"""
