from cmu_graphics import *
from PIL import Image

def onAppStart(app):
    loadImages(app)
    app.hunger = 200
    app.mood = 200
    app.stepsPerSecond = 0.1
    app.name = ''
    app.seenKeys = set()

def redrawAll(app):
    #background
    drawRect(0, 0, app.width, app.height/2, fill='orange')
    #mike's things
    # drawObjects(app, app.objectsList) 
    drawMike(app, app.width / 2, app.height/4)

    #name your mike:
    if app.name == '':
        drawLabel("Type a name for me", app.width/2, 20)
    # elif 'mike' not in app.name.lower():
    #     drawLabel("Try again...", app.width/2, 20)
    else:
        drawLabel(f'{app.name}', app.width/2 , app.height/2 - 50, size=15)

def onKeyPress(app, key):
    app.seenKeys.add(key)
    if 'enter' in app.seenKeys:
        return
    if key == 'backspace':
        app.name = app.name[:len(app.name)-1]
    if key == 'space':
        app.name += ' '
    elif len(key) == 1:
        app.name += key

def loadImages(app):
    app.images = dict()
    app.images['mike'] = Image.open('IMG_0025 4.png')
    app.images['smileMike'] = Image.open('IMG_0025 5.png')

def drawMike(app, x, y):
    #mike
    if app.hunger <= 10 or app.mood <= 10:
        mike = CMUImage(app.images['mike'])
    else:
        mike = CMUImage(app.images['smileMike'])
    drawImage(mike, x, y, align='center')
    
    if app.mood <= 10:
        drawLabel("I'm bored!", app.width/2, 20)
    elif app.hunger <= 10:
        drawLabel('Feed me!', app.width/2, 20)

    #hunger bar
    drawLabel('Hunger:', 20, app.height/2 - 30, align='left')
    drawRect(20, app.height/2 -20, app.hunger, 10, 
             align='left', fill='lightGreen')
    drawRect(20, app.height/2 -20, 200, 10, 
            align='left', fill=None, border='black')
    #mood bar
    drawLabel('Mood:', 280, app.height/2 -30, align='left')
    drawRect(280, app.height/2 -20, app.mood, 10, 
             align = 'left', fill='lightBlue')
    drawRect(app.width - 20, app.height/2 -20, 200, 10, 
            align='right', fill=None, border='black')

def drawObjects(app, objects):
    # list of stuff person bought
    for i in range(len(objects)):
        if i % 2 == 0:
            drawImage(objects[i], 20, app.height/4 + 20*i, align='center')
        else:
            drawImage(objects[i], app.width-20, app.height/4 + 20*i, align='center')
def onStep(app):
    if app.hunger > 10:
        app.hunger -= 10
    if app.mood > 10:
        app.mood -= 5
    #if task is completed: mood back to full

def main():
    runApp(500, 750)

main ()
