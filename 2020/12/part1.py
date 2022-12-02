with open("data.txt") as f:
    linesOld = f.readlines()

lines = []

for line in linesOld:
    lines.append(line.replace("\n", ""))

facing = 90

xCord = 0
yCord = 0


for item in lines:
    if item.startswith("N"):
        num = item.split("N")
        num.remove("")
        yCord += int(num[0])
    elif item.startswith("S"):
        num = item.split("S")
        num.remove("")
        yCord -= int(num[0])
    elif item.startswith("E"):
        num = item.split("E")
        num.remove("")
        xCord += int(num[0])
    elif item.startswith("W"):
        num = item.split("W")
        num.remove("")
        xCord -= int(num[0])
    elif item.startswith("L"):
        num = item.split("L")
        num.remove("")
        facing -= int(num[0])
        if facing <= -360:
            facing += 360
        if facing == -90:
            facing = 270
        elif facing == -180:
            facing = 180
        elif facing == -270:
            facing = 90
    elif item.startswith("R"):
        num = item.split("R")
        num.remove("")
        facing += int(num[0])
        if facing >= 360:
            facing -= 360
    elif item.startswith("F"):
        num = item.split("F")
        num.remove("")
        if facing == 90 or facing == -90:
            xCord += int(num[0])
        elif facing == 0 or facing == 360 or facing == -360:
            yCord += int(num[0])
        elif facing == 180 or facing == -180:
            yCord -= int(num[0])
        elif facing == 270 or facing == -270:
            xCord -= int(num[0])

if xCord < 0:
    xCord = xCord - xCord - xCord
if yCord < 0:
    yCord = yCord - yCord - yCord

senke = xCord + yCord
print(senke)
