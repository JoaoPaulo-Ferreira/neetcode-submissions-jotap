class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ndict = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in ndict:
                return [ndict[complement], idx]
            ndict[num] = idx
            

        