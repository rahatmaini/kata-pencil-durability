class pencil:

    #to initialize a pencil with its length and component durabilities
    #pass in these values as parameters during object initialization
    def __init__(self, pointDurability, leadLength, eraserDurability):
        self.originalPointDurability = pointDurability #check this to see to which durability to sharpen pencil to
        self.pointDurability = pointDurability
        self.leadLength = leadLength
        self.eraserDurability = eraserDurability
        #default values if no parameters passed? Perhaps. Easy to add after input from code review

    def sharpen():

        if (self.leadLength > 0): #if there is pencil left, sharpen it (reduce length, restore pt durability)
            self.pointDurability = self.originalPointDurability
            self.leadLength-=1
            return True #could just pass (do nothing), but this might be helpful for testing

        else:
            return False 


    def eraseText(textToErase):
        #undecided if better to implement as pencil1.eraseText("blah") or to call an erase function, passing the pencil object into it

        #needs to erase last occurence, so backwards string indexing
        #decrement eraserDurability by 1 with each character erasure
        #if eraserDurability==0, then stop erasing

        #IDEA turn string into list of characters, iterate through using for/in loop, make decisions accordingly

    def writeText(textToWrite):
        #same issue as above of indecision
        
        #just append parameter (string) to paper.


    
    #TODO editing text function

    #undecided if "paper" will be a data structure or something (pages as objects?) or a simple string will suffice, as the real testing is of the pencil and its simulation, not pages of paper or the like

    
