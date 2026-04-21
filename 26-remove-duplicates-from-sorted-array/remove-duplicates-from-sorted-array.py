class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        d={nums[i]:0 for i in range(len(nums))}
        j=0
        for i in d:
            nums[j]=i
            j+=1
        return j





        