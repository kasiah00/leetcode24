class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
         # Morse code mapping for each letter a-z
            morse_code = [
                ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
                ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
                "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
            ]
            
            # Create a set to store unique transformations
            unique_transformations = set()

            # Transform each word into Morse code
            for word in words:
                transformation = ''.join(morse_code[ord(char) - ord('a')] for char in word)
                unique_transformations.add(transformation)

            # The number of unique transformations
            return len(unique_transformations)