#given a license key represented as a string s and an integer k
#Return the reformatted license key.

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        first_group_len = len(s) % k if len(s) % k != 0 else k
        result = s[:first_group_len]
        for i in range(first_group_len, len(s), k):
            result += "-" + s[i:i +k]
        return result

