class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(k, h):
            time_to_eat = 0
            for p in piles:
                time_to_eat += ceil(p / k)
            return time_to_eat <= h
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_eat_all(mid, h):
                # slow down the monkey
                right = mid
            else:
                # speed up the monkey
                left = mid + 1
        return left
