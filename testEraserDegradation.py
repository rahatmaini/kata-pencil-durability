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

    #test to see if whitespace doesnt degrade

    #def test_ifPencilEraserIsLimitedByItsDurability(self):  

    

    

    #def tearDown(self):
    #   self.ticonderoga.dispose()

if __name__ == '__main__':
    unittest.main()