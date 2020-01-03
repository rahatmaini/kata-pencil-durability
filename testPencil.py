import unittest
import classPencil #(pointDurability, leadLength, eraserDurability)

class testPencil(unittest.TestCase):
    
    def test_sharpeningCanBeDone(self): #see if a length>0 pencil can be sharpened (should be)
        ticonderoga = classPencil.pencil(10, 2, 0) #10 pt pencil of length 2 with no eraser
        self.assertTrue(ticonderoga.sharpen())
    
    def test_sharpeningCantBeDone(self): #see if a pencil that has no length can be sharpened (should not be)
        blackwing = classPencil.pencil(10, 0, 0) #10 pt pencil of no length and no eraser
        self.assertFalse(blackwing.sharpen())


if __name__ == '__main__':
    unittest.main()