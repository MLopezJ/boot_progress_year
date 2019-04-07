blackBlock = u"\u2593"
whiteBlock = u"\u2591"
mediumBlock = u"\u2592"

def drawProgress(percent):
    bar = ''
    representationOnBar = percent / 10
    blackBlocksQuantity = int(representationOnBar)
    mediumBlockQuantity = representationOnBar - blackBlocksQuantity 
    whiteBlockQuantity = int(10-(representationOnBar))  

    while(blackBlocksQuantity > 0):
        bar+= blackBlock
        blackBlocksQuantity-= 1

    while(mediumBlockQuantity > 0):
        bar+= mediumBlock
        mediumBlockQuantity-= 1
    
    while(whiteBlockQuantity > 0):
        bar+= whiteBlock
        whiteBlockQuantity-= 1

    return(bar)


