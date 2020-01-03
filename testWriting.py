import unittest
import classPencil #(pointDurability, leadLength, eraserDurability)

class testWriting(unittest.TestCase):
    
    def setUp(self):
        self.ticonderoga = classPencil.pencil(10, 2, 0) #10 pt pencil of length 2 with no eraser
        self.page1 = "" #a piece of paper to write on

    def test_ifPaperReflectsTextWritten(self): #the pencil will write to a paper and see if the paper has that writing on it

        self.page1 = self.ticonderoga.writeText("Hello, World!", self.page1)
        self.assertEqual("Hello, World!", self.page1)

    def test_ifPaperReflectsPreviousTextAsWellAsNewWriting(self): #pencil will ADD to the paper instead of overwriting

        self.page1 = "Hello, World!"
        self.page1 = self.ticonderoga.writeText("...and Goodbye, World!", self.page1)
        self.assertEqual("Hello, World!...and Goodbye, World!", self.page1)







    #def tearDown(self):
    #   self.ticonderoga.dispose()

if __name__ == '__main__':
    unittest.main()