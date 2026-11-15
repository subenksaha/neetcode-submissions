class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            ttl = numbers[left] + numbers[right]
            if ttl == target:
                if left != right:
                    return [left+1, right+1]
                # else:
                #     right -= 1
                #     left += 1
            elif ttl > target:
                right -= 1
            else:
                left += 1
        return []