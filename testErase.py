import unittest
import classPencil #(pointDurability, leadLength, eraserDurability)

class testErase(unittest.TestCase):
    
    def setUp(self):
        self.ticonderoga = classPencil.pencil(100, 2, 100) #100 pt pencil of length 2 with 100 durability eraser
        self.page1 = "" #a piece of paper to write on

    def test_ifPencilErasesChuck(self): #from the kata readme, see if "chuck" is erased from "How much wood would a woodchuck chuck if a woodchuck could chuck wood?" and it reads "How much wood would a woodchuck chuck if a woodchuck could       wood?"
    #unfortunately this is a big test case, cannot think of a way right now to split it up. All of erase functionality is defined in this one unit test
        
        textToErase = "chuck"
        self.page1 = self.ticonderoga.writeText("How much wood would a woodchuck chuck if a woodchuck could chuck wood?", self.page1)
        self.page1 = self.ticonderoga.eraseText(textToErase, self.page1) 
        self.assertEqual("How much wood would a woodchuck chuck if a woodchuck could       wood?", self.page1)

    def test_ifPencilErasesChuckTwice(self): #same test but erasing chuck a second time as in the kata readme
        
        textToErase = "chuck"
        self.page1 = self.ticonderoga.writeText("How much wood would a woodchuck chuck if a woodchuck could chuck wood?", self.page1)
        self.page1 = self.ticonderoga.eraseText(textToErase, self.page1) 
        self.page1 = self.ticonderoga.eraseText(textToErase, self.page1) 
        self.assertEqual("How much wood would a woodchuck chuck if a wood      could       wood?", self.page1)


    #def tearDown(self):
    #   self.ticonderoga.dispose()

if __name__ == '__main__':
    unittest.main()