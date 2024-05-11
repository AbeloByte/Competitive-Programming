class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        LCP = ""
        for i in range(len(strs[0])):
            for j in strs:
                # i == len(strs[j]) --> For to fix Limitation of Bound
                if i == len(j) or j[i] != strs[0][i]:
                    return  LCP
            LCP +=strs[0][i]
        return LCP
        