import turtle


def draw_square(i, j, t, side=10, col="black"):
    x = -150 + j * side
    y = 150 - i * side
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.color(col)
    t.pendown()
    t.begin_fill()
    for k in range(4):
        t.forward(side)
        t.right(90)
    t.end_fill()
    t.penup()


# read the line from the text file
f = open("pattern.txt", "r")
line = f.readline().rstrip("\n")
f.close()

# convert '#' -> 1, ' ' -> 0
my_list = []
for ch in line:
    if ch == "#":
        my_list.append(1)
    elif ch == " ":
        my_list.append(0)

print(my_list)

# draw the pattern
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

for j in range(len(my_list)):
    if my_list[j] == 1:
        draw_square(0, j, t, 10, "black")

turtle.done()
