import unittest
import classPencil #(pointDurability, leadLength, eraserDurability)

class testPointDegradation(unittest.TestCase):
    
    def setUp(self):
        self.ticonderoga = classPencil.pencil(10, 2, 0) #10 pt pencil of length 2 with no eraser
        self.page1 = "" #a piece of paper to write on

    def test_ifPencilDegradesAfterWriting(self): #write a few characters and the pencil should degrade based on those characters
        textToWrite = "text"
        brandNewPencilDurability = self.ticonderoga.originalPointDurability
        self.page1 = self.ticonderoga.writeText(textToWrite, self.page1) 
        self.assertEqual(brandNewPencilDurability-len(textToWrite), self.ticonderoga.pointDurability)

    def test_ifPencilDegradesAfterWritingBlanks(self): #spaces should not affect pencil durability, no degradation
        textToWrite = "    "
        brandNewPencilDurability = self.ticonderoga.originalPointDurability
        self.page1 = self.ticonderoga.writeText(textToWrite, self.page1) 
        self.assertEqual(10, self.ticonderoga.pointDurability)


    #def tearDown(self):
    #   self.ticonderoga.dispose()

if __name__ == '__main__':
    unittest.main()