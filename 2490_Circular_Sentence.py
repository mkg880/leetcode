class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split()
        for i in range(len(arr)):
            if arr[i][0] != arr[i-1][-1]:
                return False
        return True