class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        s = set(folder)
        res = []
        for f in folder:
            arr = f[1:].split('/')
            tmp = ''
            b = True
            for i in range(len(arr) - 1):
                tmp += '/' + arr[i]
                if tmp in s:
                    b = False
                    break
            if b:
                res.append(f)
        return res