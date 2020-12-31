#Creates a picture of a house on green grass
#The user can click on the sun to chnage the color from yellow to orange
from graphics import *

win = GraphWin("My House", 500, 400)

sky = Rectangle(Point(0, 0), Point(500, 325))
sky.setFill('sky blue')

grass = Rectangle(Point(0, 325), Point(500, 400))
grass.setFill('green')

center = Point(75, 50)
circ = Circle(center, 30)
circ.setFill('yellow')
sky.draw(win)
grass.draw(win)
circ.draw(win)

house = Rectangle(Point(150, 150), Point(375, 325))
house.setFill('pink')
house.draw(win)

window = Rectangle(Point(200, 200), Point(250, 250))
window.setFill('grey')
window.draw(win)

door = Rectangle(Point(275, 235), Point(325, 325))
door.setFill('purple')
door.draw(win)

doorKnob = Circle(Point(315, 280), 5)
doorKnob.setFill('pink')
doorKnob.draw(win)

line1 = Line(Point(225, 200), Point(225, 250))
line1.draw(win)

line2 = Line(Point(200, 225), Point(250, 225))
line2.draw(win)

roof = Polygon(Point(150, 150), Point(260, 75), Point(375, 150))
roof.setFill('purple')
roof.draw(win)

welcome = Text(Point(260, 350), "Welcome Home!")
welcome.draw(win)

win.getMouse()
circ.setFill('orange')