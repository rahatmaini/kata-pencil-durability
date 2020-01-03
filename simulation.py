import classPencil

##basic python script to rundown all the features of a pencil as defined by the kata

def printPencilStats(pencil):
    print ("And the pencil has ", pencil.pointDurability, " point durability, ", pencil.leadLength, " length, and ", pencil.eraserDurability, " eraser durability")
    print ("\n")



ticonderoga = classPencil.pencil(30, 2, 10) #pencil with 20 pt durability, 2 length, and 10 eraser durability
page = "How" #piece of paper that says "The" on it


print ("Page currently reads: ", page)
printPencilStats(ticonderoga)


print ("Writing ' do functions creak up?'")
page = ticonderoga.writeText(" do functions creak up?", page)
#hey look at that, special characters such as "?" were not specified as how much they degrade the pencil point by. Let's presume by 2 for the sake of the kata, could be easily fixed if requirements mandated it
print ("It now reads: ", page)
printPencilStats(ticonderoga)


print ("Erasing 'creak'")
page = ticonderoga.eraseText("creak", page)
print ("It now reads: ", page)
printPencilStats(ticonderoga)

print ("Editing (through insertion) 'break'")
page = ticonderoga.editText("break", page)
print ("It now reads: ", page)
printPencilStats(ticonderoga)

print ("Sharpening")
ticonderoga.sharpen()
printPencilStats(ticonderoga)

print ("Writing ' They stop calling each other'")
page = ticonderoga.writeText(" They stop calling each other", page)
print ("It now reads: ", page)
printPencilStats(ticonderoga)


