class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums)>1:
            even, odd = sorted(nums[0::2]), sorted(nums[1::2])[::-1]
            
            for (i, elem) in enumerate(even):
                nums[i*2] = even[i]
            for (i, elem) in enumerate(odd):
                nums[i*2+1] = odd[i]
            
            return nums
        else: 
            return nums
        