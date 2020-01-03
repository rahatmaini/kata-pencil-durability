import classPencil

##basic python script to rundown all the features of a pencil as defined by the kata

def printPencilStats(pencil):
    print ("And the pencil has ", pencil.pointDurability, " point durability, ", pencil.leadLength, " length, and ", pencil.eraserDurability, " eraser durability")
    print ("\n")



ticonderoga = classPencil.pencil(30, 2, 10) #pencil with 20 pt durability, 2 length, and 10 eraser durability
page = "This" #piece of paper that says "The" on it


print ("Page currently reads: ", page)
printPencilStats(ticonderoga)


print ("Writing ' is a terrible'")
page = ticonderoga.writeText(" is a terrible", page)
print ("It now reads: ", page)
printPencilStats(ticonderoga)


print ("Erasing 'terrible'")
page = ticonderoga.eraseText("terrible", page)
print ("It now reads: ", page)
printPencilStats(ticonderoga)

print ("Editing (through insertion) 'fantastic'")
page = ticonderoga.editText("fantastic", page)
print ("It now reads: ", page)
printPencilStats(ticonderoga)

print ("Writing ' Ouija board'")
page = ticonderoga.writeText(" Ouija board", page)
print ("It now reads: ", page)
printPencilStats(ticonderoga)

print ("Sharpening")
ticonderoga.sharpen()
printPencilStats(ticonderoga)

print ("Writing 'ame for a car'")
page = ticonderoga.writeText("", page)
print ("It now reads: ", page)
printPencilStats(ticonderoga)
