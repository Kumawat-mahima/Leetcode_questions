class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = haystack.find(needle)
        return i


haystack = input()
needle = input()
str = Solution()
print(str.strStr(haystack, needle))