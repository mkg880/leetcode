class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        i = 0
        res = ''
        while num > 0:
            if num >= nums[i]:
                res += strs[i]
                num -= nums[i]
            else:
                i += 1
        return res
