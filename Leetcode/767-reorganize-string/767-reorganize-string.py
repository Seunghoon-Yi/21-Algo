class Solution:
    def reorganizeString(self, s: str) -> str:
        S = sorted(sorted(s), key = s.count)
        l = len(S)//2                         # 5 if 11 and 10.. 
        
        S[1::2], S[0::2] = S[:l], S[l:]       # 짝수에 least, 홀수에 most
        return ''.join(S)*(S[-1] != S[-2])