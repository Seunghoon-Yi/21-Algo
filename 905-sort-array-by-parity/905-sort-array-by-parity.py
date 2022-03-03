class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        
        while len(nums)!=0:
            if nums[-1]%2==0:
                even.append(nums.pop())
            else:
                odd.append(nums.pop())
        return even+odd
        