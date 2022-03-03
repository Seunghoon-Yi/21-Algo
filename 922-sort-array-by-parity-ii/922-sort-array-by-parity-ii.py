class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        if len(nums)>1 : 
            even = [i for i in nums if (i%2==0)]
            odds = [i for i in nums if (i%2==1)]
            
            #even = sorted(even)
            #odds = sorted(odds)
            
            for i in range(len(nums)//2):
                nums[i*2] = even[i]
                nums[i*2+1] = odds[i]
            return nums

        else: return nums