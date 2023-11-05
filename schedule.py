from cmu_graphics import *

def onAppStart(app):
    app.width = 500
    app.height = 750
    app.isHovering = False
    app.isHovering2 = False
    app.currPage = 1
    app.numOfPages = 3
    app.notes1 = []
    app.notes2 = []
    app.notes3 = []
    app.notes = app.notes1
    app.notesCy = 110
    app.pages = {'page1':app.notes1, 'page2':app.notes2, 'page3':app.notes3}
    app.isTransition = False
    app.transitionWidth = 0
    app.isTransition2 = False
    app.isTransitionComplete = False
    app.isWriting = False
    app.bulletPoint = ''
    app.isFull = False
    app.isDeleting = False
    app.url = 'houseImages/IMG_0025 5.png'

def redrawAll(app):
    drawRect(50, 30, 50, 20, fill='darkRed')
    drawLabel('Close', 75, 40, fill ='white')
    
    backCol = rgb(214, 246, 190)
    frontCol = rgb(229, 255, 204)
    frontPageCx = app.width/2-15
    frontPageCy = app.height/2+15
    imageWidth, imageHeight = getImageSize(app.url)
    drawImage(app.url, app.width*4/5 + 10, 60, width=imageWidth//3, 
    height=imageHeight//3, align='center')
    drawRect(frontPageCx, frontPageCy, app.width*4/5, app.height*4/5, 
             align='center', fill=frontCol)
    drawRect(app.width/2, app.height/2, app.width*4/5, app.height*4/5, 
             align='center', fill=backCol)
    for i in range(10):
        drawRect(25, 101+60*i, 50, 8, fill='lavender')
    drawLabel('Click on the notebook to add a note', 
    app.width/2, 700)
    drawLabel('Press the enter or escape key to finish a bullet point', 
    app.width/2, 715)
    delStr = 'Press d to enter delete mode and the bullet point number, d again to exit'
    drawLabel(delStr, app.width/2, 730)
    drawLabel('Notes', app.width/2, 37, size=20)
    if app.isHovering:
        points = [450, 625, 400, 625, 400, 675]
        drawPolygon(*points, fill=frontCol)
    if app.isHovering2:
        points = [100, 625, 50, 625, 100, 675]
        drawPolygon(*points, fill=frontCol)
    if app.isTransition and not app.isTransitionComplete:
        drawRect(450, 75, 1 + app.transitionWidth, 
        app.height*4/5, fill=frontCol, align='right-top')
    elif app.isTransition2 and not app.isTransitionComplete:
        drawRect(50, 75, 1 + app.transitionWidth, 
        app.height*4/5, fill=frontCol)
    if app.isTransition == False and app.isTransition2 == False:
        for i in range(len(app.notes)):
            drawCircle(90, app.notesCy+i*30, 5, fill='lavender', 
            align='left-bottom')
            drawLabel(app.notes[i], 110, app.notesCy+i*30, 
            align='left-bottom')
    if app.isFull:
        drawLabel('Your page is full!', app.width/2, 745)

def onStep(app):
    if app.currPage == 1:
        app.notes = app.pages['page1']
    elif app.currPage == 2:
        app.notes = app.pages['page2']
    elif app.currPage == 3:
        app.notes = app.pages['page3']
    if app.isTransition:
        if app.transitionWidth < app.width*4/5:
            app.transitionWidth += 10
        else:
            app.isTransitionComplete = True
            app.isTransition = False
            app.isTransition2 = False
            app.transitionWidth = 0
    if app.isTransition2:
        if app.transitionWidth < app.width*7/10:
            app.transitionWidth += 10
        else:
            app.isTransitionComplete = True
            app.isTransition = False
            app.isTransition2 = False
            app.transitionWidth = 0
    if app.isWriting:
        if (len(app.bulletPoint) != 0 and len(app.bulletPoint) % 40 == 0 
        and app.bulletPoint[-1] != '\n'):
            app.bulletPoint += '\n'
    if app.isWriting == False and app.bulletPoint != '':
        (app.notes).append(app.bulletPoint)
        app.bulletPoint = ''
    if len(app.notes) >= 19:
        app.isFull = True
    elif len(app.notes) < 19:
        app.isFull = False


def onMousePress(app, mouseX, mouseY):
    if ((mouseX >= 400) and (mouseX <= 450) and (
        mouseY >= 625) and (mouseY <= 675)):
        if app.currPage < app.numOfPages:
            app.isTransition = True
            app.isTransitionComplete = False
            app.currPage += 1
    if ((mouseX >= 50) and (mouseX <= 100) and 
          (mouseY >= 625) and (mouseY <=675)):
        if app.currPage >= 2:
            app.isTransition2 = True
            app.isTransitionComplete = False
            app.currPage -= 1
    if ((mouseX < 400) or (mouseX > 450) or (
        mouseY < 625) or (mouseY > 675)):
        if ((mouseX >= 50) and (mouseX <= 450) and 
            (mouseY > 75) and (mouseY < 675)):
            if not app.isFull:
                app.isWriting = True
    
    if 50 <= mouseX <= 100 and 30 <= mouseY <= 50:
        print("True")

def onKeyPress(app, key):
    if app.isWriting:
        if key == 'escape' or key == 'enter':
            app.isWriting = False
        elif key == 'backspace':
            app.bulletPoint = app.bulletPoint[:-1]
        elif key == 'space':
            app.bulletPoint += ' '
        elif (key != 'tab' and key != 'right' and key != 'left' and 
        key !='up' and key !='down'):
            app.bulletPoint += key
    if key == 'd':
        app.isDeleting = not app.isDeleting
    if key.isdigit():
        if app.isDeleting:
            if len(app.notes) >= (int(key) - 1) and len(app.notes) > 0:
                app.notes.pop(int(key) - 1)

    
def onMouseMove(app, mouseX, mouseY):
    if ((mouseX >= 400) and (mouseX <= 450) and 
        (mouseY >= 625) and (mouseY <= 675)):
        if app.currPage < 3:
            app.isHovering = True
    elif ((mouseX >= 50) and (mouseX <= 100) and 
          (mouseY >= 625) and (mouseY <=675)):
        if app.currPage > 1:
            app.isHovering2 = True
    else:
        app.isHovering = False  
        app.isHovering2 = False

def main():
    runApp()

main()