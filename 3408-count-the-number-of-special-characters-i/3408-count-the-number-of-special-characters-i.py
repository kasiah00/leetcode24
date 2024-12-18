class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = upper = 0 
        for ch in word: 
            if ch.islower(): lower |= 1<<ord(ch)-97
            else: upper |= 1<<ord(ch)-65
        return (lower&upper).bit_count()