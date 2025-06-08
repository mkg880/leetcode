class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        target = 0
        i = 0
        while target < len(popped):
            if stack and stack[-1] == popped[target]:
                stack.pop()
                target += 1
            else:
                while i < len(pushed) and pushed[i] != popped[target]:
                    stack.append(pushed[i])
                    i += 1
                if i == len(pushed):
                    return False
                i += 1
                target += 1
        return True