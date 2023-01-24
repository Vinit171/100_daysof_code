class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        q = set(nums)
        m = list(q)
        nums.sort()
        m.sort()
        if m==nums:
            return(False)
        else:
            return(True)