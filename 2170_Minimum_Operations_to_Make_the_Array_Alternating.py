class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        odd, even = {}, {}
        for i in range(len(nums)):
            if i % 2 == 0:
                even[nums[i]] = even.get(nums[i], 0) + 1
            else:
                odd[nums[i]] = odd.get(nums[i], 0) + 1
        first_even, first_odd, second_even, second_odd = 0, 0, 0, 0
        first_even_val, first_odd_val, second_even_val, second_odd_val = 0, 0, 0, 0
        for key in even:
            if even[key] > first_even:
                second_even, second_even_val = first_even, first_even_val
                first_even, first_even_val = even[key], key
            elif even[key] > second_even:
                second_even, second_even_val = even[key], key
        for key in odd:
            if odd[key] > first_odd:
                second_odd, second_odd_val = first_odd, first_odd_val
                first_odd, first_odd_val = odd[key], key
            elif odd[key] > second_odd:
                second_odd, second_odd_val = odd[key], key
        if first_even_val != first_odd_val:
            return n - first_even - first_odd
        keep = max(first_even + second_odd, first_odd + second_even)
        return n - keep