import math
numOfBowlingBall = int(input("How many bowling balls will be manufactured? "))
diameter = float(input("What is the diameter of each ball in inches? "))
volumeOfCore = int(input("What is the core volume in inches cubed? "))
neededFiller = ((((4 / 3) * ((math.pi) * ((diameter / 2) ** 3))) - volumeOfCore) * 100)
print("You will need ", neededFiller, " inches of cubed filler")