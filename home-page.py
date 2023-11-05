from cmu_graphics import *
from PIL import Image

def onAppStart(app):
    app.width = 500 
    app.height = 750
    app.leftMargin = 50
    app.rightMargin = 50
    app.topHeight = 350
    app.font = 'orbitron'
    app.greenPastel = rgb(193, 225, 193)

    # mike 

    # background 

    # mikecoins 
    app.mikoins = 0
    
    # menu logos 
    app.homeLogo = Image.open('menu-homeLogo.png')
    app.homeLogo = CMUImage(app.homeLogo)
    app.shopLogo = Image.open('menu-shopLogo.png')
    app.shopLogo = CMUImage(app.shopLogo)
    app.scheduleLogo = Image.open('menu-scheduleLogo.png')
    app.scheduleLogo = CMUImage(app.scheduleLogo)
    app.menuLogos = [app.homeLogo, app.shopLogo, app.scheduleLogo]

    # goals 
    app.goals = ['Sleep!', 'Eat!']
    app.checkMarksXY = []


def redrawAll(app):
    drawLine(0, app.topHeight, app.width, app.topHeight)
    # mike 

    # background 

    # mikoins 
    drawLabel(f'Mikoins: {app.mikoins}', app.leftMargin, 100, font=app.font, align='left')

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
        rectHeight = 40
        topLeftX = app.leftMargin + 40
        topLeftY = app.topHeight+110+(rectHeight+20)*i
        drawRect(topLeftX, topLeftY, app.width-app.leftMargin-app.rightMargin-50, rectHeight, align='left-top', fill=app.greenPastel)
        
        # check button
        checkButton = Image.open('goal-check.png')
        checkButton = CMUImage(checkButton)
        pilImage = checkButton.image
        buttonWidth = pilImage.width//20
        drawImage(checkButton, app.leftMargin, topLeftY+rectHeight//2, align='left', width=pilImage.width//20, height=pilImage.width//20)
        buttoncx = app.leftMargin + buttonWidth//2
        buttoncy = topLeftY + rectHeight//2 + buttonWidth//2
        # if (buttoncx, buttoncy) not in app.checkMarksXY: 
        #     app.checkMarksXY.append()

        # goal string
        goal = app.goals[i]
        drawLabel(goal, topLeftX+15, topLeftY+rectHeight//2, align='left')

def onMousePress(app, mouseX, mouseY):
    pass
    # for i in range(len(app.checkMarks)):
    #     if distance(mouseX, app)

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def main():
    runApp()

if __name__ == '__main__':
    main() 