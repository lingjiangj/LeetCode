class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        temp = ""
        for i in s:
            if i not in temp:
                temp += i
                maxLength = max(maxLength,len(temp))
            else:
                start = temp.index(i)
                temp = temp[start+1:]+i
        return maxLength
