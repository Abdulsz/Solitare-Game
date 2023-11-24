from graphics2 import*


import time


class HotAirBalloon:
    def __init__(self, color, radius, width, height, start_x, start_y):
        self.color = color
        self.radius = radius
        self.width = width
        self.height = height
        self.position = Point(start_x, start_y)
        self.balloon = Circle(self.position, self.radius)
        self.basket = Rectangle(Point(self.position.getX() - self.width/2, self.position.getY() + self.radius),
                                Point(self.position.getX() + self.width/2, self.position.getY() + self.radius + self.height))

    def draw(self, win):
        self.balloon.setFill(self.color)
        self.balloon.setOutline("black")
        self.balloon.draw(win)

        self.basket.setFill(self.color)
        self.basket.setOutline("black")
        self.basket.draw(win)

    def undraw(self):
        if self.balloon:
            self.balloon.undraw()
        if self.basket:
            self.basket.undraw()

    def move_up(self, distance):
        self.position.move(0, -distance)
        self.balloon.move(0, -distance)
        self.basket.move(0, -distance)

def simulate_race():
    win_width = 400
    win_height = 400
    balloon_radius = 50
    basket_width = 40
    basket_height = 20
    start_x1 = 100
    start_x2 = 300
    start_y = win_height - balloon_radius
    distance_per_step = 10
    delay = 0.1

    win = GraphWin("Hot Air Balloon Race", win_width, win_height)

    balloon1 = HotAirBalloon("red", balloon_radius, basket_width, basket_height, start_x1, start_y)
    balloon2 = HotAirBalloon("blue", balloon_radius, basket_width, basket_height, start_x2, start_y)

    balloon1.draw(win)
    balloon2.draw(win)

    start_text = Text(Point(win_width/2, win_height/2), "Click to start the race!")
    start_text.setSize(20)
    start_text.draw(win)

    win.getMouse()  # Wait for user click

    start_text.undraw()

    while balloon1.position.getY() > balloon_radius and balloon2.position.getY() > balloon_radius:
        balloon1.move_up(distance_per_step)
        balloon1.undraw()
        balloon1.draw(win)
        time.sleep(delay)

        balloon2.move_up(distance_per_step)
        balloon2.undraw()
        balloon2.draw(win)
        time.sleep(delay)

    if balloon1.position.getY() <= balloon_radius:
        winner = "Red Balloon"
    else:
        winner = "Blue Balloon"

    winner_text = Text(Point(win_width/2, win_height/2), f"The winner is: {winner}!")
    winner_text.setSize(20)
    winner_text.draw(win)

    win.getMouse()
    win.close()

    return winner

# Simulate the race and print the winner
winner = simulate_race()
print(f"The winner is: {winner}!")