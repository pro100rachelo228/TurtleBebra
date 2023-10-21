lines = ""
with open(input(),"r") as s:
    lines = s.readlines()

# -------------------------------

# generators
# filter (map)
# try | except


import turtle
import re
import lib
    

commands = [
    lib.SetColorRGB,
    lib.SetColorWord,
    lib.BeginFill,
    lib.EndFill,
    lib.Forward,
    lib.Left,
    lib.Rigth,
    lib.Up,
    lib.Down,
    lib.GoTo,
    lib.Circle,
    lib.Width,
    lib.Speed,
    lib.Square,
]

with open("actions.log", "w") as fl:
    for line in lines: 
        if line.isspace() or line == "" or line[0] == "#":
            continue
        done = False
        for cmd in commands:
            match = re.match(cmd.source(), line)
            if match != None:     
                print(cmd.action(match),file=fl)
                done = True
                break
        if not done:
            print(f"Unknown command: {line}",file=fl)    

turtle.exitonclick()