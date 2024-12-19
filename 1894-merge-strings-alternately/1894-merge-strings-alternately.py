class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []  # Use a list to accumulate the characters
        l = min(len(word1), len(word2))
        
        for i in range(l):
            output.append(word1[i])
            output.append(word2[i])
        
        # Append the remaining parts of word1 or word2, if any
        output.append(word1[l:])
        output.append(word2[l:])
        
        return "".join(output)