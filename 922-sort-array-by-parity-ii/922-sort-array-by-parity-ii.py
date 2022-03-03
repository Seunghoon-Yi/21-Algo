class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        if len(nums)>1 : 
            even, odds = [],[]
            for elem in nums:
                if elem%2==0 : even.append(elem)
                else: odds.append(elem)
            even = sorted(even)
            odds = sorted(odds)
            for i in range(len(nums)//2):
                nums[i*2] = even[i]
                nums[i*2+1] = odds[i]
            return nums

        else: return nums