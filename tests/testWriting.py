import unittest

import sys
sys.path.append("..")

import classPencil #(pointDurability, leadLength, eraserDurability)

class testWriting(unittest.TestCase):
    
    def setUp(self):
        self.ticonderoga = classPencil.pencil(100, 2, 0) #100 pt pencil of length 2 with no eraser
        self.page1 = "" #a piece of paper to write on

    def test_ifPaperReflectsTextWritten(self): #the pencil will write to a paper and see if the paper has that writing on it

        self.page1 = self.ticonderoga.writeText("Hello, World!", self.page1)
        self.assertEqual("Hello, World!", self.page1)

    def test_ifPaperReflectsPreviousTextAsWellAsNewWriting(self): #pencil will ADD to the paper instead of overwriting

        self.page1 = "She sells sea shells"
        self.page1 = self.ticonderoga.writeText(" down by the sea shore", self.page1)
        self.assertEqual("She sells sea shells down by the sea shore", self.page1)



    #def tearDown(self):
    #   self.ticonderoga.dispose()

if __name__ == '__main__':
    unittest.main()