class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word == word.lower():
            return True
        
        word1 = word[1:]

        if word1 == word1.lower():
            return True
