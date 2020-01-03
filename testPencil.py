import unittest
import classPencil #(pointDurability, leadLength, eraserDurability)

class testPencil(unittest.TestCase):
    
    def test_sharpeningCanBeDone(self): #see if a valid pencil can be sharpened, as intended
        ticonderoga = classPencil.pencil(10, 2, 0) #10 pt pencil of length 2 with no eraser
        self.assertTrue(ticonderoga.sharpen())
    
    


if __name__ == '__main__':
    unittest.main()