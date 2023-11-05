from cmu_graphics import *

def onAppStart(app):
    app.year = "2023"
    app.month = "November"
    app.days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    app.active_fieldCal = None
    app.fieldCal_colors = {"Year": "gray", "Month": "gray", "Day": ["white"] * 31}
    app.fieldCal_texts = {"Year": "2023", "Month": "November", "Day": ""}
    app.day = ""
    
    app.width = 500  # Set the width to 500 pixels
    app.height = 750  # Set the height to 750 pixels
    app.fields = ["Task:", "Add Tag:", "Description:", 'Schedule Date:']
    app.field_texts = ["", "", "", ""]
    app.active_field = None
    app.field_colors = ["gray", "gray", "gray", "gray"]
    app.tagBold = [False,False,False]

    app.close = False

def redrawAll(app):
    y = 100
    drawLabel('Schedule a Task!', 250, y-50, size=20, align='center')
    drawRect(400, 30, 50, 20, fill='darkRed')
    drawLabel('Close', 425, 40, fill ='white')
    for i in range(len(app.fields)-1):
        label = app.fields[i]
        field_text = app.field_texts[i]
        field_color = app.field_colors[i]
        drawLabel(label, 50, y, size=16, align='left')
        if i == 1:
            drawLabel('Work', 200, y+5, align='left', size=16, bold=app.tagBold[0])
            drawLabel('Rest/Wellness', 200 + 52, y+5, align='left', size=16, bold=app.tagBold[1])
            drawLabel('Exercise', 200 + 170, y+5, align='left', size=16, bold=app.tagBold[2])
        else:
            drawRect(200, y - 10, 250, 30, fill=field_color)
            # Display the field text in the box
            drawLabel(field_text, 210, y + 5, align='left')
        y += 50
    drawLabel(app.fields[3] + ' ' + app.day, 50, y, size=16, align='left')
    drawCalendar(app)

def drawCalendar(app):
    drawRect(170,285,75,20, fill = app.fieldCal_colors['Year'], align='center')
    drawRect(300,285,100,20, fill = app.fieldCal_colors['Month'], align='center')
    drawLabel(app.fieldCal_texts["Year"], 170, 285, size=16, align='center')
    drawLabel(app.fieldCal_texts["Month"], 300, 285, size=14, align='center')

    y = 300
    for i in range(len(app.days)):
        day = app.days[i]
        day_color = app.fieldCal_colors["Day"][i]
        # Display the day box
        drawRect(75 + (i % 7) * 50, y + (i // 7) * 50, 50, 50, fill=day_color)
        # Display the day text in the box
        drawLabel(day, 100 + (i % 7) * 50, y + 25 + (i // 7) * 50)

def onMousePress(app, mouseX, mouseY):
    y = 100
    for i in range(len(app.fields)):
        if 200 <= mouseX <= 450 and y - 10 <= mouseY <= y + 20:
            if 140 <= mouseY <= 170:
                if 200 <= mouseX <= 200 + 52:
                    app.field_texts[1] = 'Work'
                    app.tagBold = [False,False,False]
                    app.tagBold[0] = True
                elif 200 + 52 <= mouseX <= 200 + 170:
                    app.field_texts[1] = 'Rest/Wellness'
                    app.tagBold = [False,False,False]
                    app.tagBold[1] = True
                else:
                    app.field_texts[1] = 'Exercise'
                    app.tagBold = [False,False,False]
                    app.tagBold[2] = True
            else:
                app.active_field = i
                app.field_colors[i] = "green"
        y += 50

    for i in range(len(app.days)):
        if 100 + (i % 7) * 50 <= mouseX <= 200 + (i % 7) * 50 and 300 + (i // 7) * 50 <= mouseY <= 350 + (i // 7) * 50:
            app.active_fieldCal = "Day"
            app.fieldCal_colors["Day"] = ["white"] * 31  # Reset all days to white
            app.fieldCal_colors["Day"][i] = "green"  # Set the selected day to green
            app.day = app.days[i] + ' ' +  app.fieldCal_texts["Month"] + ' ' + app.fieldCal_texts["Year"]

    if 170 <= mouseX <= 175+75 and 285 <= mouseY <= 305:
        app.active_fieldCal = "Year"
        app.fieldCal_colors["Year"] = "green"
        app.fieldCal_colors["Day"] = ["white"] * 31  # Reset all days to white

    if 300 <= mouseX <= 400 and 285 <= mouseY <= 305:
        app.active_fieldCal = "Month"
        app.fieldCal_colors["Month"] = "green"
        app.fieldCal_colors["Day"] = ["white"] * 31  # Reset all days to white
    
    if 400 <= mouseX <= 450 and 30 <= mouseY <= 50:
        app.close = True
        app.field_texts[3] = app.day
        print('True', app.field_texts)

def onKeyPress(app, key):
    if app.active_field is not None:
        if key == "enter":
            app.field_colors[app.active_field] = "white"
            app.active_field = None
        elif key == "backspace":
            if app.field_texts[app.active_field]:
                app.field_texts[app.active_field] = app.field_texts[app.active_field][:-1]
        elif key == 'space':
            app.field_texts[app.active_field] += ' '
        else:
            app.field_texts[app.active_field] += key
    
    if app.active_fieldCal == "Year" or app.active_fieldCal == "Month":
        if key == "enter":
            app.fieldCal_colors[app.active_fieldCal] = "white"
            app.active_fieldCal = None
        elif key == "backspace":
            if app.fieldCal_texts[app.active_fieldCal]:
                app.fieldCal_texts[app.active_fieldCal] = app.fieldCal_texts[app.active_fieldCal][:-1]
        elif key == 'space':
            app.field_texts[app.active_field] += ' '
        else:
            app.fieldCal_texts[app.active_fieldCal] += key

def main():
    runApp(500, 750)
    
if __name__ == '__main__':
    main()
