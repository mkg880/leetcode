class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num < 2:
            return num == 0
        for i in range(num // 2, num):
            rev = int(str(i)[::-1])
            if rev + i == num:
                return True
        return False