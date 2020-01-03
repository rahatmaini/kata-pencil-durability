import unittest
import classPencil #(pointDurability, leadLength, eraserDurability)

class testEditing(unittest.TestCase):
    
    def setUp(self):
        self.ticonderoga = classPencil.pencil(100, 2, 5) #100 pt pencil of length 2 with eraser durability 5
        self.page1 = "" #a piece of paper to write on

    def test_ifPencilEraserIsDegradingAfterErasing(self):  #test to see "onion" can be successfully inserted after erasing
        textToInsert = "onion"
        textToErase = "apple"

        self.page1 = self.ticonderoga.writeText("An apple a day keeps the doctor away", self.page1)
        self.page1 = self.ticonderoga.eraseText(textToErase, self.page1) 

        self.page1 = self.ticonderoga.editText("onion", self.page1)
        self.assertEqual("An onion a day keeps the doctor away", self.page1)

    def test_checkTextCollisions(self): #test to see if new text is longer than allocated whitespace, then collisions result in "@"
        textToInsert = "artichoke"
        textToErase = "apple"

        self.page1 = self.ticonderoga.writeText("An apple a day keeps the doctor away", self.page1)
        self.page1 = self.ticonderoga.eraseText(textToErase, self.page1) 

        self.page1 = self.ticonderoga.editText("artichoke", self.page1)
        self.assertEqual("An artich@k@ay keeps the doctor away", self.page1)
  

    #def tearDown(self):
    #   self.ticonderoga.dispose()

if __name__ == '__main__':
    unittest.main()