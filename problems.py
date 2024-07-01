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

# 88. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n != 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return nums1
        if n == 0:
            return nums1
        for i in range(len(nums2)):
            nums1[m+i] = nums2[i]
        return nums1.sort()

# 485. Max Consecutive Ones
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = []
        cnt = 0
        for i in nums:
            if i == 1:
                cnt+= 1
            else:
                l.append(cnt)
                cnt = 0
        l.append(cnt)
        return max(l)

# 977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            l.append(i*i)
        return sorted(l)

# 1089. Duplicate Zeros
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        l = []
        zeros = 0
        for i in arr:
            if i == 0:
                zeros += 1
        i = n - 1
        while zeros > 0:
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
            i -= 1

# 1295. Find Numbers with Even Number of Digits
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                l +=1
        return l

# 27. Remove element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = i = 0
        while(i < len(nums)):
            if nums[i] == val:
                cnt += 1
                nums.pop(i)
            else:
                i += 1
        return len(nums)

# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
        return len(nums)

