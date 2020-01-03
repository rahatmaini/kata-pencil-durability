import unittest

import sys
sys.path.append("..")

import classPencil #(pointDurability, leadLength, eraserDurability)

class testEraserDegradation(unittest.TestCase):
    
    def setUp(self):
        self.ticonderoga = classPencil.pencil(100, 2, 3) #100 pt pencil of length 2 with eraser durability 3
        self.page1 = "" #a piece of paper to write on

    def test_ifPencilEraserIsDegradingAfterErasing(self):  #test to see if eraser is degrading per character (dont worry about whitespaces in this test)
        textToErase = "World"
        self.page1 = self.ticonderoga.writeText("Hello, World", self.page1)
        self.page1 = self.ticonderoga.eraseText(textToErase, self.page1) 
        self.assertEqual(0, self.ticonderoga.eraserDurability) #wont even successfully erase everything, not durable enough

    def test_ifWhitespaceDoesntCauseDegradation(self): #test to make sure whitespace doesnt degrade
        textToErase = "  "
        self.page1 = self.ticonderoga.writeText("Hello,  World", self.page1) #2 spaces now
        self.page1 = self.ticonderoga.eraseText(textToErase, self.page1) 
        self.assertEqual(3, self.ticonderoga.eraserDurability) #should be same eraser durability as out of box

    def test_ifPencilEraserIsLimitedByItsDurability(self): #make sure if the eraser has been run down to 0, it cannot erase. test case right from kata github readme
        textToErase = "Bill"
        self.page1 = self.ticonderoga.writeText("Buffalo Bill", self.page1) #2 spaces now
        self.page1 = self.ticonderoga.eraseText(textToErase, self.page1) 
        self.assertEqual("Buffalo B   ", self.page1)

    

    #def tearDown(self):
    #   self.ticonderoga.dispose()

if __name__ == '__main__':
    unittest.main()