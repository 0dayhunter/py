import turtle

def bresenham_line(x1, y1, x2, y2):
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    x_step, y_step = (1, 1) if x1 < x2 else (-1, -1)
    error, line_points = 2 * dy - dx, []
    x, y = x1, y1

    for _ in range(dx + 1):
        line_points.append((x, y))
        if error > 0:
            y += y_step
            error -= 2 * dx
        error += 2 * dy
        x += x_step

    return line_points

# Example usage
turtle.setup(500, 500)
turtle.speed(0)

x1, y1, x2, y2 = 100, 100, 400, 300
line_points = bresenham_line(x1, y1, x2, y2)

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
for x, y in line_points:
    turtle.goto(x, y)

turtle.exitonclick()
