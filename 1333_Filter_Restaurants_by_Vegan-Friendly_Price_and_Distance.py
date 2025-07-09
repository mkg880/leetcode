class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        arr = []
        for i, r, v, p, d in restaurants:
            if (not veganFriendly or v) and p <= maxPrice and d <= maxDistance:
                arr.append([-r, -i])
        arr.sort()
        return [-x for _, x in arr]