import pgzrun
from random import randint
player = Actor("player", (400, 550))
DIFFICULTY = 1


def draw():
    screen.blit('background', (0, 0))
    player.draw()
    drawAlien()
    drawBases()
    drawLasers()


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
    updateLasers()
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
    global moveDelay, moveCounter, moveSequence, lasers
    initAliens()
    initBases()
    lasers = []
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
    global player, lasers
    if keyboard.left and player.x > 40:
        player.x -= 5
    if keyboard.right and player.x < 760:
        player.x += 5
    if keyboard.space:
        l = len(lasers)
        lasers.append(Actor("laser2", (player.x, player.y-32)))
        lasers[l].status = 0
        lasers[l].type = 1


def drawLasers():
    for l in range(len(lasers)):
        lasers[l].draw()


def updateLasers():
    global lasers, aliens
    for l in range(len(lasers)):
        if lasers[l].type == 0:
            lasers[l].y += (2*DIFFICULTY)
            checkLaserHit(l)
            if lasers[l].y > 600:
                lasers[l].status = 1
        if lasers[l].type == 1:
            lasers[l].y -= 5
            checkPlayerLaserHit(l)
            if lasers[l].y < 10:
                lasers[l].status = 1
    lasers = listCleanup(lasers)
    aliens = listCleanup(aliens)


def listCleanup(liste):
    return liste


def checkPlayerLaserHit(l):
    pass


def checkLaserHit(l):
    pass


init()
pgzrun.go()
