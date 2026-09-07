class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited_nums = set()
        for num in range(0, len(nums)):
            if nums[num] in visited_nums:
                return True
            else:
                visited_nums.add(nums[num])
        return False










