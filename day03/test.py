file = open('sample-1.txt', 'r')
engineSchematics = []
gearNumbers = [] # here we store all the gear numbers
starPositions = [] # here we store coordinates of a star
gearParts = [] # here we store a number that is next to the star. The i-th number is adjacent of the star with the coordinates stored on the i-th position in starPositions

for line in file:
    line = line.strip()
    engineSchematics.append(line)

def checkForSymbols(lineNo, colNoStart, colNoEnd): # function where we check for a start adjacent to the number on line lineNo, starting at position colNoStart and ends at position colNoEnd

    if colNoStart > 0: #if the line doesn't begins with the number 
        startCheck = colNoStart - 1 # we can check before it
        if engineSchematics[lineNo][startCheck]=='*': # if there is a * before the number
            if [lineNo, startCheck] in starPositions: # if this star position is already in starPositions (meaning this is the second number adjacent to this star - so this star is a gear)
                gearNumbers.append(int(engineSchematics[lineNo][colNoStart:colNoEnd+1])*gearParts[starPositions.index([lineNo, startCheck])]) # we store this star gear number to gearNumbers - it's counted as: this number x number from gearParts that was store on the same position as the coordinates of this star
            else: # this star position is not yet in starPositions - this is the first number adjacent to this start we came across so far
                starPositions.append([lineNo, startCheck]) # we append this star position to the starPositions
                gearParts.append(int(engineSchematics[lineNo][colNoStart:colNoEnd+1])) # we append this number to the gearParts
    else: # line lineNo starts with this number
        startCheck = 0 # we can't check before

    if colNoEnd == len(engineSchematics[0]) - 1: #same, just for checking after the number on the same line
        endCheck = colNoEnd
    else:
        endCheck = colNoEnd + 1
       
        if engineSchematics[lineNo][endCheck]=='*':
            if [lineNo, endCheck] in starPositions:
                gearNumbers.append(int(engineSchematics[lineNo][colNoStart:colNoEnd+1])*gearParts[starPositions.index([lineNo, endCheck])])
            else:
                starPositions.append([lineNo, endCheck])
                gearParts.append(int(engineSchematics[lineNo][colNoStart:colNoEnd+1]))
    

    if lineNo > 0: # if the number is not on the first (0th) line we can similarly check there if there is a star adjacent
        for i in range(startCheck, endCheck + 1):
            if engineSchematics[lineNo-1][i]=='*':
                if [lineNo-1, i] in starPositions:
                    gearNumbers.append(int(engineSchematics[lineNo][colNoStart:colNoEnd+1])*gearParts[starPositions.index([lineNo-1, i])])
                else:
                    starPositions.append([lineNo-1, i])
                    gearParts.append(int(engineSchematics[lineNo][colNoStart:colNoEnd+1]))

    if lineNo < len(engineSchematics) - 1: # if the number is not on the last line we can similarly check there if there is a star adjacent
        for i in range(startCheck, endCheck + 1):
            if engineSchematics[lineNo+1][i]=='*':
                if [lineNo+1, i] in starPositions:
                    gearNumbers.append(int(engineSchematics[lineNo][colNoStart:colNoEnd+1])*gearParts[starPositions.index([lineNo+1, i])])
                else:
                    starPositions.append([lineNo+1, i])
                    gearParts.append(int(engineSchematics[lineNo][colNoStart:colNoEnd+1]))

for lineNo in range(len(engineSchematics)): # we again check lines one by one
    colNo = 0 # and characters in them one by one
    while colNo < len(engineSchematics[0]): # until we reach the end of a line we repeat
        if engineSchematics[lineNo][colNo].isdigit(): # if we find a digit we get its first position and  last position
            start = colNo
            colNo +=1
            while colNo < len(engineSchematics[lineNo]) and engineSchematics[lineNo][colNo].isdigit():
                colNo +=1
            end = colNo - 1
            checkForSymbols(lineNo, start, end) # checking for a star adjacent to this number
        colNo +=1
print(engineSchematics)
print(gearNumbers)
print(sum(gearNumbers))