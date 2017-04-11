#This Progra ives the total number of items present in the data structure




list={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayinventory(l):
    total = 0
    print "Inventory:"
    for a,b in l.items():
        print b,a
        total=total+b
    print "total number of items ",total

displayinventory(list)
