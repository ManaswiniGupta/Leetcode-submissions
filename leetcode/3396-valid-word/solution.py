class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vowel=0
        consonant=0
        num=0
        for i in word:
            if i.isalnum():
                if i.isalpha():
                    if i.lower() in 'aeiou':
                        vowel=1
                    else:
                        consonant=1
               
            else:
                return False
        if vowel==1 and consonant==1:
            return True
        return False
        
                    


        
