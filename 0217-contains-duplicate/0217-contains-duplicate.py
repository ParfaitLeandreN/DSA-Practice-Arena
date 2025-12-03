class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # ## HASHSET

        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
            
        #     seen.add(num)
        # return False


        # ## SORTING
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False


        # ## BRUTE FORCE
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False


        ## HASHSET LENGTH
        return len(set(nums)) != len(nums)