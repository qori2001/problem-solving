from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n
        nums_ = []
        while i < n and n < len(nums):
            nums_.append( nums[i])
            nums_.append(nums[n])
            i+=1
            n+=1
        return nums_


solution = Solution()

print(solution.shuffle([1,2,3,4,4,3,2,1],4))


