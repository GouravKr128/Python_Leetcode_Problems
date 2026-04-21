# Time Complexity -> O(nxm)
# n -> lenghth on strs
# m -> length of shortest string
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        indx=0
        min_len = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i])<min_len:
                min_len = len(strs[i])
                indx = i
        min_str = strs[indx]
        d={ i:min_str[i] for i in range(len(min_str))}
        flag = True
        for i in d:
            for s in strs:
                if s[i]==d[i]:
                    pass
                else:
                    flag = False
                    break
            else:
                output=output+d[i]

            if flag == False:
                break

        return output

        