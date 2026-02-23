class Solution(object):
    def checkIfPangram(self, sentence):
        sentence = sentence.lower()
        alpha = "abcdefghijklmnopqrstuvwxyz"
        
        for letter in alpha:
            if letter not in sentence:
                return False
        
        return True