class Solution:
    def arrangeWords(self, text: str) -> str:
        arr = text.split()
        arr[0] = arr[0].lower()
        arr.sort(key=lambda x: len(x))
        arr[0] = arr[0][0].upper() + arr[0][1:]
        return ' '.join(arr)