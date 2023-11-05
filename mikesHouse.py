from cmu_graphics import *
from PIL import Image
import createGoals

def onAppStart(app):
    loadImages(app)
    app.hunger = 200
    app.mood = 200
    app.stepsPerSecond = 0.1
    app.name = ''
    app.seenKeys = set()
    app.food = None
    app.objectsList = None

    app.leftMargin = 50
    app.rightMargin = 50
    app.topHeight = 370
    app.font = 'orbitron'
    app.greenPastel = rgb(193, 225, 193)

    # mikecoins 
    app.mikecoins = 0

    # menu logos 
    app.homeLogo = Image.open('houseImages/menu-homeLogo.png')
    app.homeLogo = CMUImage(app.homeLogo)
    app.shopLogo = Image.open('houseImages/menu-shopLogo.png')
    app.shopLogo = CMUImage(app.shopLogo)
    app.scheduleLogo = Image.open('houseImages/menu-notePadLogo.png')
    app.scheduleLogo = CMUImage(app.scheduleLogo)
    app.menuLogos = [app.homeLogo, app.shopLogo, app.scheduleLogo]

    # goals 
    app.goals = ['Sleep!', 'Eat!']
    app.rectHeight = 40 
    app.rectWidth = app.width-app.leftMargin-app.rightMargin-50
    app.checkMarkRadius = 20 
    updateCheckAndRectLists(app)

    # add new goal 
    app.plusButton = Image.open('houseImages/goal-AddNew.png')
    app.plusButton = CMUImage(app.plusButton)
    app.plusPilImage = app.plusButton.image
    app.plusWidth = app.plusPilImage.width // 15
    app.close = False 

def redrawAll(app):
    #background
    drawRect(0, 0, app.width, app.height/2, fill='orange')
    #mike's things
    drawObjects(app) 
    drawMike(app, app.width / 2, app.height/4)

    #name your mike:
    if app.name == '':
        drawLabel("Type a name for me and press 'enter'", app.width/2, 20)
    # elif 'mike' not in app.name.lower():
    #     drawLabel("Try again...", app.width/2, 20)
    else:
        drawLabel(f'{app.name}', app.width/2 , app.height/2 - 50, size=15)

    #how much money you have
    drawLabel(f'Mike Coins: {app.mikecoins}', app.width -20, 20, align='right')

    #inventory
    drawInventory(app)

    # menu 
    for i in range(len(app.menuLogos)): 
        logo = app.menuLogos[i]
        pilImage = logo.image
        drawImage(logo, 150+i*100, app.topHeight+40, align='center',
                width=pilImage.width//13,
                height=pilImage.height//13)


    # goals left for today 
    numGoalsLeft = len(app.goals)
    drawLabel(f'{numGoalsLeft} goals left for today!', app.leftMargin, app.topHeight+90, font=app.font, align='left')
    for i in range(len(app.goals)): 
        # rectangle
        topLeftX, topLeftY = app.rectsTopLeft[i]
        drawRect(topLeftX, topLeftY, app.rectWidth, app.rectHeight, align='left-top', fill=app.greenPastel)
        
        # check button
        checkCX, checkCY = app.checkMarksXY[i]
        drawCircle(checkCX, checkCY, app.checkMarkRadius, fill=app.checkMarksColors[i], border='orange', borderWidth=4)

        # goal string
        goal = app.goals[i]
        drawLabel(goal, topLeftX+15, topLeftY+app.rectHeight//2, align='left')
    
    # add new goal 
    drawImage(app.plusButton, app.width//2, app.height-40, align='center', 
              width=app.plusWidth, height=app.plusWidth)

# ---------------------- CHECKMARK BUTTONS
def updateCheckAndRectLists(app):
    app.rectsTopLeft = []
    app.checkMarksXY = []
    app.checkMarksColors = []
    
    for i in range(len(app.goals)):
        # rectangles 
        topLeftX = app.leftMargin + 60
        topLeftY = app.topHeight+110+(app.rectHeight+20)*i
        app.rectsTopLeft.append((topLeftX, topLeftY))
        
        # checkmarks 
        checkMarkCX = app.leftMargin + app.checkMarkRadius 
        checkMarkCY = topLeftY + app.checkMarkRadius 
        app.checkMarksXY.append((checkMarkCX, checkMarkCY))
        app.checkMarksColors.append(None)

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def getGoalIndex(app, mouseX, mouseY, checkMarksXYList):
    for i in range(len(checkMarksXYList)):
        checkMarkCX, checkMarkCY = checkMarksXYList[i]
        if distance(mouseX, mouseY, checkMarkCX, checkMarkCY) <= app.checkMarkRadius: 
            return i 
    return None 

def onMousePress(app, mouseX, mouseY):
    # goals checkmarks 
    i = getGoalIndex(app, mouseX, mouseY, app.checkMarksXY)
    if i != None: 
        app.goals.pop(i)
        updateCheckAndRectLists(app)
    
    # add new goal 
    plusRadius = app.plusWidth // 2
    plusCX = app.width // 2
    plusCY = app.height - 40 
    if distance(mouseX, mouseY, plusCX, plusCY) <= plusRadius: 
        print('createGoals')

def onMouseMove(app, mouseX, mouseY):
    i = getGoalIndex(app, mouseX, mouseY, app.checkMarksXY)
    if i != None:
        app.checkMarksColors[i] = 'orange'
    else:
        for j in range(len(app.checkMarksColors)):
            app.checkMarksColors[j] = None

# ---------------------- MIKE'S HOUSE

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
    app.images['mike'] = Image.open('houseImages/IMG_0025 4.png')
    app.images['smileMike'] = Image.open('houseImages/IMG_0025 5.png')

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

def drawObjects(app):
    # list of stuff person bought
    if app.objectsList == None: return
    for i in range(len(app.objectsList)):
        if i % 2 == 0:
            drawImage(app.objectsList[i], 20, app.height/4 + 20*i, align='center')
        else:
            drawImage(app.objectsList[i], app.width-20, 
                      app.height/4 + 20*i, align='center')

def drawInventory(app):
    drawLabel('Your stuff:', app.width-20, 50, align='right')
    if app.food == None: return
    for i in range(len(app.food)):
        drawImage(app.food[i], app.width-20, app.height/4 + 20*i, align='center')


def onStep(app):
    if app.hunger > 10:
        app.hunger -= 10
    if app.mood > 10:
        app.mood -= 5
    #if task is completed: mood back to full

def main():
    runApp(500, 750)
    if app.close: 
        return True 

if __name__ == '__main__':
    main()
    