import turtle as t

turtle = t.Turtle()


class Command: 

    def source():
        return ""
        
    def action(match):
        return ""

#------------------------------------------------------------------------------------

class SetColorRGB(Command):

    def source():
        return r"color *(\d+.\d+) *(\d+.\d+) *(\d+.\d+)"
    
    def action(match):
        turtle.color(float(match.group(1)) ,float(match.group(2)), float(match.group(3)))
        return f'Set color to "{match.group(1)}, {match.group(2)}, {match.group(3)}"'

class SetColorWord(Command):

    def source():
        return r"color *(\w+)"
    
    def action(match):
        turtle.color(match.group(1))
        return f'Set color to "{match.group(1)}"'

class BeginFill(Command):

    def source():
        return r"begin *fill"
    
    def action(match):
        turtle.begin_fill()
        return 'Start filling'

class EndFill(Command):


    def source():
        return r"end *fill"

    def action(match):
        turtle.end_fill()
        return 'End filling'
    
class Forward(Command):

    def source():
        return r"forward +(-?\d+)"
        
    def action(match):
        turtle.forward(float(match.group(1)))
        return f'Move forward "{match.group(1)}"'
    
class Left(Command):

    def source():
        return r"left +(-?\d+)"
        
    def action(match):
        turtle.left(float(match.group(1)))
        return f'Turn left {match.group(1)} degrees'
    
class Rigth(Command):

    def source():
        return r"right +(-?\d+)"
        
    def action(match):
        turtle.right(float(match.group(1)))
        return r"right +(-?\d+)"
    
class Up(Command):

    def source():
        return r"up"
        
    def action(match):
        turtle.up()
        return 'Up'    
    
class Down(Command):
    
    def source():
        return r"down"
        
    def action(match):
        turtle.down()
        return 'Down'  

class GoTo(Command):
    
    def source():
        return r"goto +(-?\d+) +(-?\d+)"
        
    def action(match):
        turtle.goto(float(match.group(1)), float(match.group(2)))
        return f'Go to {match.group(1)}, {match.group(2)}'     

class Circle(Command):

    def source():
        return r"circle +(\d+)"
        
    def action(match):
        turtle.circle(float(match.group(1)))
        return f"Circle with radius {match.group(1)}"   
    
class Width(Command):
    
    def source():
        return r"width +(\d+)"
        
    def action(match):
        turtle.width(float(match.group(1)))
        return f'Width {match.group(1)}'
    
class Speed(Command):
     
    def source():
        return r"speed +(\d+)"
        
    def action(match):
        turtle.speed(float(match.group(1)))
        return f'Speed {match.group(1)}'  
    
class Square(Command):
     
    def source():
        return r"square +(\d+)"
        
    def action(match):
        for i in range(4):
            turtle.fd(float(match.group(1)))
            turtle.right(90)
        return f'Square {match.group(1)}'  
    

    