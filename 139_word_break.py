'''
Intuition:
    DP. Memoize the indexes in which a matched word ended.
    For every word, see if it comes after an already matched word.
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
            for i in range(1, len(s) + 1):
                for word in wordDict:
                    if dp[i-1] == True and s[i-1:i+len(word)-1] == word:
                            dp[i+len(word)-1] = True
        return dp[-1]                                                                                 
