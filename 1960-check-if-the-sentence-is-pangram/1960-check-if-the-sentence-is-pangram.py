class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a=len(set(sentence))
        if a==26:
            return True 
        else:
            return False
        