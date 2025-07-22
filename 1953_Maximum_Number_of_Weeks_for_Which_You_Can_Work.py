class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        most = max(milestones)
        curr = sum(milestones) - most
        add = min(most, curr+1)
        return curr + add