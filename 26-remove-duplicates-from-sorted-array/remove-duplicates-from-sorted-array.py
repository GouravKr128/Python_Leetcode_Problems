class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        i=1
        first_duplicate=None
        while True:
            if i==first_duplicate:
                return i
            if nums[i]==nums[i-1]:
                nums.append(nums.pop(i-1))
                if first_duplicate == None:
                    first_duplicate=len(nums)-1
                else:
                    first_duplicate-=1

            else:
                if (i+1)==len(nums):
                    return i+1
                else:
                    i+=1


        