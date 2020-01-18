import pgzrun
import math
from random import randint

player = Actor("player", (400, 550))
DIFFICULTY = 1


def draw():
    screen.blit('background', (0, 0))
    player.image = player.images[math.floor(player.status/6)]
    player.draw()
    drawLasers()
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
        if randint(0, 5) == 0:
            lasers.append(Actor("laser1", (alien.x, alien.y)))
            lasers[len(lasers)-1].status = 0
            lasers[len(lasers)-1].type = 0
    moveSequence += 1
    if moveSequence == 40:
        moveSequence = 0


def update():
    global moveCounter, player
    checkKeys()
    updateLasers()
    moveCounter += 1
    if moveCounter == moveDelay:
        moveCounter = 0
        updateAliens()
    if player.status > 0:
        player.status += 1


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
            bases[bc].collideLaser = collideLaser.__get__(bases[bc])
            bases[bc].height = 60
            bc += 1


def drawBases():
    for base in bases:
        base.drawClipped()


def init():
    global lasers, score, player, moveSequence, moveCounter, moveDelay
    initAliens()
    initBases()
    moveCounter = 0
    moveSequence = 0
    player.status = 0
    score = 0
    player.laserCountdown = 0
    lasers = []
    moveDelay = 30
    player.images = ["player", "explosion1", "explosion2",
                     "explosion3", "explosion4", "explosion5"]
    player.laserActive = 1


def initAliens():
    global aliens
    aliens = []
    for a in range(18):
        aliens.append(Actor('alien1',
                            (210 + (a % 6) * 80, 100 + (a // 6) * 64)))
        aliens[a].status = 0


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


def makeLaserActive():
    global player
    player.laserActive = 1


def drawLasers():
    for l in range(len(lasers)):
        lasers[l].draw()


def updateLasers():
    global lasers, aliens
    for laser in lasers:
        if laser.type == 0:
            laser.y += (2*DIFFICULTY)
            checkLaserHit(laser)
            if laser.y > 600:
                laser.status = 1
        if laser.type == 1:
            laser.y -= 5
            checkPlayerLaserHit(laser)
            if laser.y < 10:
                laser.status = 1
    lasers = listCleanup(lasers)
    aliens = listCleanup(aliens)


def collideLaser(self, other):
    return (
        self.x-20 < other.x+5 and
        self.y-self.height+30 < other.y and
        self.x+32 > other.x+5 and
        self.y-self.height+30 + self.height > other.y
    )


def listCleanup(l):
    newList = []
    for i in l:
        if i.status == 0:
            newList.append(i)
    return newList


def checkPlayerLaserHit(l):
    for b in bases:
        if b.collideLaser(l):
            l.status = 1
    for a in aliens:
        if a.collidepoint((l.x, l.y)):
            l.status = 1
            a.status = 1


def checkLaserHit(l):
    global player
    if player.collidepoint((l.x, l.y)):
        player.status = 1
        l.status = 1
    for b in bases:
        if b.collideLaser(l):
            b.height -= 10
            l.status = 1


init()
pgzrun.go()
