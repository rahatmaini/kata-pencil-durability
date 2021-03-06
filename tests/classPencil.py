class pencil:

    #to initialize a pencil with its length and component durabilities
    #pass in these values as parameters during object initialization
    def __init__(self, pointDurability, leadLength, eraserDurability):
        self.originalPointDurability = pointDurability #check this to see to which durability to sharpen pencil to
        self.pointDurability = pointDurability
        self.leadLength = leadLength
        self.eraserDurability = eraserDurability

        self.stackOfErasurePoints = [] #stack of points where pencil erased last
        #MIGHT want to move this over to being something that pages keep track of rather than pencils
        #this could be point of conversation during code review
        #might switch pencils when writing on piece of paper! Important to be able to substitute
        #but for now, for KISS implementation of pencil, let's keep it this way :)

        #default values if no parameters passed? Perhaps. Easy to add after input from code review




    def sharpen(self):

        if (self.leadLength > 0): #if there is pencil left, sharpen it (reduce length, restore pt durability)
            self.pointDurability = self.originalPointDurability
            self.leadLength-=1
            return True #could just pass (do nothing), but this might be helpful for testing

        else:
            return False 




    #assumption: pencil will not try to erase words that dont exist
    def eraseText(self, textToErase, paperToWriteOnto):

        reversedTextToErase = textToErase[::-1]
        paperToWriteOnto = paperToWriteOnto[::-1] 
        #from the perspective of the eraser, we see the page backwards first (think of it as right to left)


        whereToBeginErasing = paperToWriteOnto.find(reversedTextToErase) #find where text that needs to be erased occurs, then starting from that index out to the length of that text just replace with blanks.
        paperToWriteOnto = list(paperToWriteOnto)


        #for use in editing text, add last erase point to the stack to see where the last erasure was so we know where to insert when that function is called
        #-1 index returns most recent erasure. instead of a stack and a list, could very well be an int of the last erasure. point of discussion, depends on requirements (do we want a history of erasures?)

        i = whereToBeginErasing
        j = 0
        while (j < len(reversedTextToErase)): #replacing each char to be erased with a " "

            if (paperToWriteOnto[i] == " "):
                self.stackOfErasurePoints.append(len(paperToWriteOnto) - i - 1) #how to not repeat myself?
            elif (self.eraserDurability > 0):
                self.stackOfErasurePoints.append(len(paperToWriteOnto) - i - 1) #repeat statement, would like to architect this logic better. please guide me, dear kata reviewer
                self.eraserDurability -= 1
                paperToWriteOnto[i] = " "
            else:
                pass
            i+=1 #incrementer on the page of where the eraser is 
            j+=1 #incrementer on the phrase to erase, of where in that phrase we are

        return convertListOfCharsToString(paperToWriteOnto)[::-1] #convert list of chars into string then reverse it back to normal for perspective of pencil/writer




    def writeText(self, textToWrite, paperToWriteOnto):
        
        allTheTextToWrite = list(textToWrite) #have a list of chars in the text to write

        for char in allTheTextToWrite: #
            paperToWriteOnto += self.returnTextToBeWritten(char)

        return paperToWriteOnto


    def editText(self, textToWrite, paperToWriteOnto):

        allTheTextToInsert = list(textToWrite)
        allTextOnPaper = list(paperToWriteOnto)

        i = self.stackOfErasurePoints[-1] #where to start inserting
        j = 0
        while (j < len(textToWrite)):
            if (allTextOnPaper[i] == " "):
                allTextOnPaper[i] = self.returnTextToBeWritten(allTheTextToInsert[j])
            else:
                #assuming a collision results in chickenscratch looking "@" but the writting is still there, capital or lowercase, and the pencil tip is degraded accordingly 
                if (self.returnTextToBeWritten(allTheTextToInsert[j]) != " "): #call helper func
                    allTextOnPaper[i] = "@" 
            j+=1
            i+=1

            #There is a problem if you erase and want to edit something into the very end of the page. This is a fix for that (essentially passes the rest of what needs to be added to the writeText function to be appended as normal). Caught this bug during refactoring
            if (i>=len(allTextOnPaper)):
                paperToWriteOnto = convertListOfCharsToString(allTextOnPaper)
                return self.writeText(convertListOfCharsToString(allTheTextToInsert[j:]),paperToWriteOnto)
        
        return convertListOfCharsToString(allTextOnPaper)
    

    def returnTextToBeWritten(self, char): #handles durability checking, decrementing, and returns the char to write (whether a blank or a char)
    #DRY! this simplifies writing and editing text
    
        #as long as the pencil will be at 0 or more pointyness, we can write
        #otherwise add a blank space instead of the character that was supposed to be added

        if (self.pointDurability - returnWeightOfCharacterWritten(char) >= 0): 
            self.pointDurability -= returnWeightOfCharacterWritten(char)
            return char
        else:
            return " "







##HELPER FUNCTIONS BELOW##

def returnWeightOfCharacterWritten(char): #pretty sure char isnt a reserved keyword in python, we'd figure it out during peer code review before production no sweat

    if (char == " "):
        return 0
    elif (char.upper()==char):
        return 2
    elif (char.lower()==char):
        return 1

def convertListOfCharsToString(listOfChars): #take a list of chars and turn it into one string
    s = ""
    for char in listOfChars:
        s+=char
    return s