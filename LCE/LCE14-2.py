#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()

        first_str = strs[0]
        last_str = strs[-1]

        common_prefix = []
        for i in range(len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            else:
                break
        return "".join(common_prefix)


'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs=sorted(strs) #strs is Input List
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first), len(last))):
            if(first[i]!= last[i]):
                return ans
            ans+=first[i]
        return ans


        for s in range(len(str)):
            if s == len(str) - 1 and s == len(str + 1):
                return str
            repeat()
        else:
            return ""
'''        