'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''

# fuck this "easy" problem, took me 2 fucking hours
class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # empty
        if not strs:
            return ""

        # iterate through each letter of the first string
        for i in range(len(strs[0])):
            char = strs[0][i] # getting each letter from the first word
            for string in strs[1:]: # from next string to the last

                # checks if the length of the first string is greater than or the same as the current string
                # also checks if the current character at the current string is not the same as the character from the first string
                # if any of those condition is true, return the the index needed to get the longest prefix
                # we can apply the first condition, since if the longest prefix is longer than the first string, then it's not common in every string
                if i >= len(string) or string[i] != char: 
                    return strs[0][:i] # [:i] slices from start of the string to the specified index
        
        return strs[0] # when all matches, just return the first string or any string in general
            
        # NOTE TO SELF
        # list[specifiedIndex:] starts from specified index to the end of the list

    # THIS SOLUTION IS BULLSHIT, WHY DOES PYTHON HAVE THIS FUNCTION?!
        import os 
        class Solution(object):
            def longestCommonPrefix(self, strs):
                pref = os.path.commonprefix(strs)

                return pref 
            
    # THIS SOLUTION IS SIMILAR TO MINE, WHY DIDN'T I THINK OF THIS?
        class Solution(object):
            def longestCommonPrefix(self, strs):
                """
                :type strs: List[str]
                :rtype: str
                """

                # check if empty
                if not strs:
                    return ""
            
                # this for the prefix
                str2 = ""

                # iterate through the entire first string
                for i in range(len(strs[0])): 
                    # iterate from next string to last
                    # same as mine, no fancy operations
                    for j in range(1, len(strs)): 
                        # same conditon 
                        if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                            return str2 # return if any condition met
                        
                    # append the current character that's the same in the prefix string
                    str2 += strs[0][i]
                return str2