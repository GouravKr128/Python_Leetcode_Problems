class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        i=0
        j=1
        while j!=len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                i+=1
                nums[i]=nums[j]
                j+=1
        return i+1



""" 2nd Method:-
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
"""




        