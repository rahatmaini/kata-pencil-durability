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

        print (self.page1)
        self.assertEqual("An onion a day keeps the doctor away", self.page1)

  

    #def tearDown(self):
    #   self.ticonderoga.dispose()

if __name__ == '__main__':
    unittest.main()