class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        if len(nums)>1:
            aux_list = [0]*len(nums)
            anc_even, anc_odd = 0, 1
            
            for elem in nums:
                if elem%2 == 0:
                    aux_list[anc_even] = elem
                    anc_even+=2
                else:
                    aux_list[anc_odd] = elem
                    anc_odd+=2
            return aux_list
        
        else: return aux_list