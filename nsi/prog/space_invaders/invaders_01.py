import pgzrun
player = Actor("player", (400, 550))


def draw():
    screen.blit('background', (0, 0))
    player.draw()


def update():
    pass


def init():
    pass


pgzrun.go()
