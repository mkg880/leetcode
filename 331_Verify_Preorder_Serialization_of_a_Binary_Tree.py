class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        arr = preorder.split(',')
        i = 0
        def rec():
            nonlocal i
            if i >= len(arr):
                return False
            if arr[i] != '#':
                i += 1
                return rec() and rec()
            else:
                i += 1
                return True
        return rec() and i == len(arr)