from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        return [key for key, value in sorted_freq[:k]]