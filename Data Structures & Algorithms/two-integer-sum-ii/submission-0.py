from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            value = numbers[left] + numbers[right]

            if value == target:
                return [left + 1, right + 1]
            
            if left < right and value < target:
                left += 1
            
            elif left < right and value > target:
                right -= 1
        return []