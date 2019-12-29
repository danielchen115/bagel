'''
Intuition:
    Really cool yet simple DP problem. Works almost like
    mathematical induction. at every step, we can either choose
    to steal from the last house (which means we can't steal from the
    current house) OR we can steal from the 2nd last house and steal from
    this one. At every step, we take the max of the two.
'''
class Solution:
        def rob(self, nums: List[int]) -> int:
                last1 = 0
                last2 = 0
                for i in range(len(nums)):
                    last2, last1 = last1, max(last1, last2 + nums[i])
                return last1
                                                                
