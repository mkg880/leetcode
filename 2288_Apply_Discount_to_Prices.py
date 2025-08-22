class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        arr = sentence.split()
        p = (100 - discount) / 100
        for i, word in enumerate(arr):
            if word[0] == '$':
                price = word[1:]
                if price.isdigit():
                    arr[i] = '$' + f"{int(price) * p:.2f}"
        return ' '.join(arr)