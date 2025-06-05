class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split('.')
        arr2 = version2.split('.')
        i = 0
        j = 0
        while i < len(arr1) or j < len(arr2):
            a = int(arr1[i]) if i < len(arr1) else 0
            b = int(arr2[j]) if j < len(arr2) else 0
            if a < b:
                return -1
            if b < a:
                return 1
            i += 1
            j += 1
        return 0