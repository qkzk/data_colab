import pgzrun
from random import randint
player = Actor("player", (400, 550))


def draw():
    screen.blit('background', (0, 0))
    player.draw()
    drawAlien()
    drawBases()


def drawAlien():
    for alien in aliens:
        alien.draw()


def updateAliens():
    global moveSequence, moveDelay
    movex = movey = 0
    if moveSequence < 10 or moveSequence > 30:
        movex = -15
    if moveSequence == 10 or moveSequence == 30:
        movey = 50
    if moveSequence > 10 and moveSequence < 30:
        movex = 15
    for alien in aliens:
        animate(alien, pos=(alien.x + movex, alien.y + movey),
                duration=0.5, tween='linear')
        if randint(0, 1) == 0:
            alien.image = "alien1"
        else:
            alien.image = "alien1b"
    moveSequence += 1
    if moveSequence == 40:
        moveSequence = 0


def update():
    global moveCounter
    checkKeys()
    moveCounter += 1
    if moveCounter == moveDelay:
        moveCounter = 0
        updateAliens()


def drawClipped(self):
    screen.surface.blit(self._surf, (self.x - 32, self.y-self.height + 30),
                        (0, 0, 64, self.height))


def initBases():
    global bases
    bases = []
    bc = 0
    for b in range(3):
        for p in range(3):
            bases.append(Actor("base1", midbottom=(150+(b*200)+(p*40), 520)))
            bases[bc].drawClipped = drawClipped.__get__(bases[bc])
            bases[bc].height = 60
            bc += 1


def drawBases():
    for base in bases:
        base.drawClipped()


def init():
    global moveDelay, moveCounter, moveSequence
    initAliens()
    initBases()
    moveDelay = 30
    moveCounter = 0
    moveSequence = 0


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
