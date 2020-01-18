import pgzrun
player = Actor("player", (400, 550))


def draw():
    screen.blit('background', (0, 0))
    player.draw()
    for alien in aliens:
        alien.draw()


def update():
    checkKeys()


def init():
    initAliens()


def initAliens():
    global aliens
    aliens = []
    for a in range(18):
        aliens.append(Actor('alien1',
                            (210 + (a % 6) * 80, 100 + (a // 6) * 64)))


def checkKeys():
    global player
    if keyboard.left and player.x > 40:
        player.x -= 5
    if keyboard.right and player.x < 760:
        player.x += 5


init()
pgzrun.go()
