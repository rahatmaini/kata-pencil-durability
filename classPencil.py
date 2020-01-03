class pencil:

    #to initialize a pencil with its length and component durabilities
    #pass in these values as parameters during object initialization
    def __init__(self, pointDurability, leadLength, eraserDurability):
        self.originalPointDurability = pointDurability #check this to see to which durability to sharpen pencil to
        self.pointDurability = pointDurability
        self.leadLength = leadLength
        self.eraserDurability = eraserDurability
        #default values if no parameters passed? Perhaps. Easy to add after input from code review

    def sharpen(self):

        if (self.leadLength > 0): #if there is pencil left, sharpen it (reduce length, restore pt durability)
            self.pointDurability = self.originalPointDurability
            self.leadLength-=1
            return True #could just pass (do nothing), but this might be helpful for testing

        else:
            return False 


    #def eraseText(self, textToErase):
        #undecided if better to implement as pencil1.eraseText("blah") or to call an erase function, passing the pencil object into it

        #needs to erase last occurence, so backwards string indexing
        #decrement eraserDurability by 1 with each character erasure
        #if eraserDurability==0, then stop erasing

        #IDEA turn string into list of characters, iterate through using for/in loop, make decisions accordingly

    def writeText(self, textToWrite, paperToWriteOnto):
        
        allTheText = list(textToWrite) #have a list of chars in the text to write

        for char in allTheText:
            if (char != " "):
                self.pointDurability -= 1
            else:
                pass
            paperToWriteOnto += char
            
        return paperToWriteOnto


    

    
