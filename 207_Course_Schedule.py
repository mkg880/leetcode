class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            m[a].append(b)
        while m:
            rem = None
            for key in m:
                if m[key] == []:
                    rem = key
                    break
            if rem == None:
                return False
            del m[rem]
            for key in m:
                if rem in m[key]:
                    m[key].remove(rem)
        return True