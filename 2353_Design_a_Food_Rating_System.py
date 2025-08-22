import heapq


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings = {}
        self.cuisines = {}
        self.f_to_c = {}
        for f, c, r in zip(foods, cuisines, ratings):
            if c not in self.cuisines:
                self.cuisines[c] = []
            heapq.heappush(self.cuisines[c], (-r, f))
            self.ratings[f] = r
            self.f_to_c[f] = c

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[food] = newRating
        heapq.heappush(self.cuisines[self.f_to_c[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisines[cuisine]
        while heap:
            rating, food = heapq.heappop(heap)
            if self.ratings[food] == -rating:
                heapq.heappush(heap, (rating, food))
                return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)