"""
Python file containing solutions to LeetCode problems
"""

# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i, value in enumerate(nums):
            r = target - nums[i]

            if r in x:
                return [i, x[r]]
            else:
                x[value] = i


# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        z = x
        while x > 0:
            d = x % 10
            reverse = reverse * 10 + d
            x //= 10
        
        if reverse == z:
            return True
        else:
            return False

# 13. Roman to Integer - Can be made much simpler
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        x = 0
        sk = False
        if len(s) == 1:
            return d[s]
        for i, c in enumerate(s[:-1]):
            if sk:
                sk = False
                continue
            if c == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                x = x + d[s[i+1]] - 1
                sk = True
            elif c == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                x = x + d[s[i+1]] - 10
                sk = True
            elif c == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                x = x + d[s[i+1]] - 100
                sk = True
            else:
                x = x + d[c]
        if not sk and len(s) > 1:
            x = x + d[s[-1]]
        return x


# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        l = min(len(x) for x in strs)
        for i in range(l):
            cnt = 0
            ch = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] == ch:
                    cnt += 1
                else:
                    return s
            if cnt == len(strs):
                s += ch
        return s


