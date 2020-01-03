import unittest
import classPencil #(pointDurability, leadLength, eraserDurability)

class testEraserDegradation(unittest.TestCase):
    
    def setUp(self):
        self.ticonderoga = classPencil.pencil(100, 2, 6) #100 pt pencil of length 2 with eraser durability 5
        self.page1 = "" #a piece of paper to write on

    def test_ifPencilEraserIsDegradingAfterErasing(self):  #test to see if eraser is degrading per character (dont worry about whitespaces in this test)
        textToErase = "World!"
        self.page1 = self.ticonderoga.writeText("Hello, World", self.page1)
        self.page1 = self.ticonderoga.eraseText(textToErase, self.page1) 
        self.assertEqual(0, self.ticonderoga.eraserDurability)

    def test_ifWhitespaceDoesntCauseDegradation(self): #test to make sure whitespace doesnt degrade
        textToErase = "  "
        self.page1 = self.ticonderoga.writeText("Hello,  World", self.page1) #2 spaces now
        self.page1 = self.ticonderoga.eraseText(textToErase, self.page1) 
        self.assertEqual(6, self.ticonderoga.eraserDurability) #should be same eraser durability as out of box

    #def test_ifPencilEraserIsLimitedByItsDurability(self):  

    

    

    #def tearDown(self):
    #   self.ticonderoga.dispose()

if __name__ == '__main__':
    unittest.main()