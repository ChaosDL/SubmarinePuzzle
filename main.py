import random
lowestPosition=0
lowestVelocity=1
subPosition = int(input("Enter an int for sub position\n"))#random.randint(lowestPosition,10)
subVelocity = int(input("Enter an int for sub velocity\n"))#random.randint(lowestVelocity,10)
currentPosition = 0
currentVelocity = 1
#True means the coordinates are counted in a clockwise path i.e. scale units right, scale units down, in the path of a top right corner. False means the coords are counted in a ccw path i.e. scale units up, scale units left
rightCornerCW = True
#How many units a direction is moved. Is increased by one everytime rightCornerCW is alternated
scale = 1
#Counters keep track of how many more positions need to be counted for each position and velocity, are set to scale after reaching 0
positionCounter = scale
velocityCounter = scale
time=0
#Checks and sets counters to scale if both are 0, alternates rightCornerCW
def checkCounters():
	global rightCornerCW, scale, positionCounter, velocityCounter
	if positionCounter==0 and velocityCounter==0 :
		rightCornerCW = not rightCornerCW
		scale +=1
		positionCounter, velocityCounter = scale, scale
#Calculates the next pair of position and velocity to test according to path
def nextPair():
	global currentPosition, lowestPosition 
	global currentVelocity, lowestVelocity
	global rightCornerCW, scale, positionCounter, velocityCounter
#	If both counters have been exhausted, i.e. the corner is completed, change corner path direction, increase scale, and set counters to scale
	if rightCornerCW :
		if positionCounter>0:
			currentPosition, positionCounter = currentPosition+1, positionCounter-1
		else:
			currentVelocity, velocityCounter = currentVelocity-1, velocityCounter-1
	else:
		if velocityCounter>0:
			currentVelocity, velocityCounter = currentVelocity+1, velocityCounter-1
		else:
			currentPosition, positionCounter = currentPosition-1, positionCounter-1
	checkCounters()
	return(currentPosition, currentVelocity)
#Checks if it's appropriate to increment position or velocity. Called before nextPair
def considerLowPositions():
	global currentPosition, lowestPosition 
	global currentVelocity, lowestVelocity
	global rightCornerCW
	if currentPosition == lowestPosition and rightCornerCW :
		currentVelocity +=1
		return(currentPosition, currentVelocity)
	if currentVelocity == lowestVelocity and not rightCornerCW :
		currentPosition += 1
		return(currentPosition, currentVelocity)
#Returns a submarine's current position based on initial position, velocity, and the current time
def positionToHit(testInitialPosition, testVelocity, currentTime):
	return testInitialPosition + testVelocity*currentTime

def main():
	global subPosition, subVelocity, time
	coords = (currentPosition, currentVelocity)
	lowConsidered = False
	while( subPosition != positionToHit(coords[0], coords[1], time)):
		print(coords)
		time += 1 #Increment time
		subPosition += subVelocity #Increment submarine's position
		if not lowConsidered:
			coords = considerLowPositions()
			lowConsidered = True
			if coords is not None: continue
		if lowConsidered:
			coords=nextPair()
			lowConsidered = False
	print("Sub initial pos: " + str(currentPosition), "Sub vel: " + str(currentVelocity), "Time :" + str(time), "Sub current pos:" + str(subPosition))
main()
#try using two booleans instead of the continue for fun
