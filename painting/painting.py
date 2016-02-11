import numpy
import sys


def paintSquare(picture,row,col,boxwidth):
	for iRow in range(row,row+boxwidth):
		for iCol in range(col,col+boxwidth):
			picture[iRow][iCol] = paint(picture[iRow][iCol])
	return picture

def paintSquare2(picture,row,col,boxwidth):
	for iRow in range(row,row+boxwidth):
		for iCol in range(col,col+boxwidth):
			picture[iRow][iCol] = 1
	return picture

def paintHLine(picture,r,c1,c2):
	for iCol in range(c1,c2+1):
			picture[r][iCol] = paint(picture[r][iCol])
	return picture

def paintHLine2(picture,r,c1,c2):
	for iCol in range(c1,c2+1):
			picture[r][iCol] = 1
	return picture

def paintVLine(picture,r1,r2,c):
	for iRow in range(r1,r2+1):
		picture[iRow][c] = paint(picture[iRow][c])
	return picture

def paintVLine2(picture,r1,r2,c):
	for iRow in range(r1,r2+1):
		picture[iRow][c] = 1
	return picture


def paint(pixel):
	if pixel == 1:
		pixel = 2
	elif pixel == 0:
		pixel = -1
	return pixel

def findBestLineLength(line):
	bestLineCount = 0
	bestEndpoint = 0
	if(line[0]==1):
		for idx in xrange(len(line),0,-1):
			lineCount = (line[0:idx]).count(1)-(line[0:idx]).count(0)
			if(lineCount>=bestLineCount):
				bestLineCount = lineCount
				bestEndpoint = idx -1
	return (bestLineCount,bestEndpoint)

def findBestBox(picture,r,c,n,m):
	bestBoxCount = 0
	bestS = 0
	sMax = min(r,c,n-r,m-c)
	if(sMax>0):
		for s in xrange(sMax,0,-1):
			box = [row[c-s:c+s+1] for row in picture[r-s:r+s+1]]
			boxCount = sum(row.count(1)-row.count(0) for row in box)
			if(boxCount>bestBoxCount):
				bestBoxCount = boxCount
				bestS = s
	return (bestBoxCount,bestS)



def paintPicture(filename):
	#Read file and create binary matrix
	#filename = "smallTest"
	f = open(filename+".in","r")
	commandList = []
	header = f.readline()
	[n,m]=[int(i) for i in header.split()]
	picture = [[0 for i in range(m)] for j in range(n)]

	for iRow in range(n):
		lineIn = f.readline()
		for iCol in range(m):
			picture[iRow][iCol] = 0 if lineIn[iCol] == "." else 1;

	newPicture = [[0 for i in range(m)] for j in range(n)]

	#Fill with boxes with s>0
#	sMax = min((m-1)/2,(n-1)/2)
#	for s in xrange(sMax,0,-1):
#		boxwidth = 2*s+1
#		for iRow in xrange(n-boxwidth+1):
#			for iCol in xrange(m-boxwidth+1):
#				box = [row[iCol:iCol+boxwidth] for row in picture[iRow:iRow+boxwidth]]
#				nUnpainted = sum(row.count(1) for row in box)
#				if nUnpainted > boxwidth*(boxwidth-1):
#					r=iRow+boxwidth/2
#					c=iCol+boxwidth/2
#					commandList.append("PAINT_SQUARE %s %s %s\n" %(r,c,s))
#					picture = paintSquare(picture,iRow,iCol,boxwidth)
#					newPicture = paintSquare2(newPicture,iRow,iCol,boxwidth)


	#Fill with horizontal lines and vertical lines

	for iRow in xrange(n):
		for iCol in xrange(m):
			hLine = picture[iRow][iCol:]
			vLine = [row[iCol] for row in picture[iRow:]]
			(hBestLineCount,hBestEndpoint) = findBestLineLength(hLine)
			(vBestLineCount,vBestEndpoint) = findBestLineLength(vLine)
			(bestBoxCount,bestS) = findBestBox(picture,iRow,iCol,n,m)
			#if(bestBoxCount>max(hBestLineCount,vBestLineCount)):
			#	r=iRow
			#	c=iCol
			#	s=bestS
			#	commandList.append("PAINT_SQUARE %s %s %s\n" %(r,c,s))
			#	picture = paintSquare(picture,iRow-s,iCol-s,2*s+1)
			#	newPicture = paintSquare2(newPicture,iRow-s,iCol-s,2*s+1)
			if(hBestLineCount>vBestLineCount and hBestLineCount>0):
				r1 = iRow
				r2 = iRow
				c1 = iCol
				c2 = iCol + hBestEndpoint
				commandList.append("PAINT_LINE %s %s %s %s\n" %(r1, c1, r2, c2))
				picture = paintHLine(picture,r1,c1,c2)
				newPicture = paintHLine2(newPicture,r1,c1,c2)
			elif(vBestLineCount>0):
				r1 = iRow
				r2 = iRow + vBestEndpoint
				c1 = iCol
				c2 = iCol
				commandList.append("PAINT_LINE %s %s %s %s\n" %(r1, c1, r2, c2))
				picture = paintVLine(picture,r1,r2,c1)
				newPicture = paintVLine2(newPicture,r1,r2,c1)


	#Clear cells
	for iRow in xrange(n):
			for iCol in xrange(m):
				if picture[iRow][iCol]==-1:
					commandList.append("ERASE_CELL %s %s\n" %(iRow,iCol))
					picture[iRow][iCol] = 0
					newPicture[iRow][iCol] = 0
				elif picture[iRow][iCol] == 2:
					picture[iRow][iCol] = 1


	#Write to file
	nCommands = len(commandList)
	fOut = open(filename+".out","w")
	fOut.write("%s\n" %nCommands)
	for command in commandList:
		fOut.write(command)
	fOut.close()



paintPicture(sys.argv[1])