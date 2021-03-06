import Myro
from Myro import *
from Graphics import *
from random import *

width = 500
height = 500
sim = Simulation("Maze World", width, height, Color("gray"))

#outside walls
sim.addWall((10, 10), (490, 20), Color("black"))
sim.addWall((10, 10), (20, 490), Color("black"))
sim.addWall((480, 10), (490, 490), Color("black"))
sim.addWall((10, 480), (490, 490), Color("black"))

#blue spot
poly = Circle((50, 50), 45)
poly.bodyType = "static"
poly.color = Color("blue")
poly.outline = Color("black")
sim.addShape(poly)

#red spot
poly = Circle((450, 50), 45)
poly.bodyType = "static"
poly.color = Color("red")
poly.outline = Color("black")
sim.addShape(poly)

#green spot
poly = Circle((50, 450), 45)
poly.bodyType = "static"
poly.color = Color("green")
poly.outline = Color("black")
sim.addShape(poly)

#yellow spot
poly = Circle((450, 450), 45)
poly.bodyType = "static"
poly.color = Color("yellow")
poly.outline = Color("black")
sim.addShape(poly)

#begin simulation and sets robot's position
makeRobot("SimScribbler", sim)
sim.setPose(0, width/2, height/2, 0)

sim.setup()

# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

#The following is a helper function 
#Inputs: A picture and a color represented by the list above
#Returns the average x location of the color in the picture or -1 if the robot has found the color spot

def findColorSpot(picture, color):
    xPixelSum = 0
    totalPixelNum = 0
    averageXPixel = 0

    show(picture)

    for pixel in getPixels(picture):
        if(color == 1 and getRed(pixel) > 150 and getGreen(pixel) < 50 and getBlue(pixel) < 50):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 2 and getRed(pixel) < 50 and getGreen(pixel) > 100 and getBlue(pixel) < 50):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 3 and getRed(pixel) < 50 and getGreen(pixel) < 50  and getBlue(pixel) > 150):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 4 and getRed(pixel) > 200 and getGreen(pixel) > 150 and getBlue(pixel) < 50):
            
            xPixelSum += getX(pixel)
            totalPixelNum += 1
    if(totalPixelNum != 0):
        averageXPixel = xPixelSum/totalPixelNum

    #Handles the case where robot has found the spot if it is near it
    #If necessary adjust the value
    if(totalPixelNum/(getWidth(picture)*getHeight(picture)) > 0.21):
        averageXPixel = -1

    return averageXPixel


# Use the following integers for colors:
# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

######################Code Starts Here##################################

turnBy(randrange(1,360))

red=int(1)
green=int(2)
blue=int(3)
yellow=int(4)

pic = takePicture()

def go_blob():
    forward(1,3.75)
    pic = takePicture()
    show(pic)
    backward(1,3.75)

getWidth(pic)
x = findColorSpot(pic,1)
print(x)

while x != 0:
    go_blob()
    

#colors=input("What color would you like to go to? (Red = 1, Blue = 2, Green = 3, Yellow = 4)")

#def go_red():
    #turnBy(45)
    #forward(1,3.75)
    #pic = takePicture()
    #show(pic)
    #backward(1,3.75)
    #turnBy(-45)

#def go_blue():
    #turnBy(135)
    #forward(1,3.75)
    #pic = takePicture()
    #show(pic)
    #backward(1,3.75)
    #turnBy(-135)

#def go_yellow():
    #turnBy(-45)
    #forward(1,3.75)
    #pic = takePicture()
    #show(pic)
    #backward(1,3.75)
    #turnBy(45)
    
#def go_green():
    #turnBy(-135)
    #forward(1,3.75)
    #pic = takePicture()
    #show(pic)
    #backward(1,3.75)
    #turnBy(135)

#red = 1
#blue = 2
#green = 3
#yellow = 4

#if colors == "1":
    #go_red()
#elif colors == "2":
    #go_blue()
#elif colors == "3":
    #go_green()
#elif colors == "4":
    #go_yellow()
#else:
    #stop()