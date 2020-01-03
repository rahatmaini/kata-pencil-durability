import unittest

import sys
sys.path.append("..")

import classPencil #(pointDurability, leadLength, eraserDurability)

class testSharpening(unittest.TestCase):
    
    def setUp(self):
        self.ticonderoga = classPencil.pencil(10, 2, 0) #10 pt pencil of length 2 with no eraser
        self.page1 = "" #a piece of paper to write on

    def test_sharpeningCanBeDone(self): #see if a length>0 pencil can be sharpened (should be)

        self.assertTrue(self.ticonderoga.sharpen())
    
    def test_sharpeningCantBeDone(self): #see if a pencil that has no length can be sharpened (should not be)

        self.ticonderoga.leadLength=0
        self.assertFalse(self.ticonderoga.sharpen())

    def test_sharpenedToOriginalDurability(self): #see if sharpening pencil returns it to original durability
        
        self.ticonderoga.pointDurability-=5 #TODO return to this test once writing has been implemented. 
        self.ticonderoga.sharpen()
        self.assertEqual(10,self.ticonderoga.pointDurability) #sharpened ticonderoga should have 10 durability



    #def tearDown(self):
    #   self.ticonderoga.dispose()

if __name__ == '__main__':
    unittest.main()