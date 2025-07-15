class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        starting = 0
        while starting < n and binary[starting] == '1':
            starting += 1
        if starting == n:
            return binary
        ones = binary[starting:].count('1')
        return '1' * (n - ones - 1) + '0' + '1' * ones