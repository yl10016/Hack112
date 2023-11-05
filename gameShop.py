from cmu_graphics import *
from PIL import Image

def onAppStart(app):
    app.width = 500
    app.height = 750
    app.money = 1000  # Initial amount of money
    app.inventory = []  # User's inventory
    app.item_images = []
    app.item_descriptions = []
    app.item_costs = []
    app.active_item = None
    app.name = 'createdName'
    
    # Load and store item images
    app.item_names = ['chair.png', 'axolotl.jpeg', 'onesie.jpeg', 'patvirtue.webp']
    for item in app.item_names:
        app.item_images.append(CMUImage(Image.open(f'shopImages/{item}')))
    
    # Item descriptions and costs
    app.item_descriptions = [
        f"A comfortable chair for {app.name}'s home.",
        "A cute pet axolotl.",
        "A cozy onesie for Halloween.",
        "Pat Virtue?!"
    ]
    app.item_costs = [50, 100, 150, 10000]
    app.displayed = set(app.inventory)

def redrawAll(app):
    drawLabel(f"Game Shop!", app.width/2, 50, size=20, align='center')
    # Display user's money in the top right corner
    drawLabel(f"Available Funds: ${app.money}", app.width - 50, 75, size=12, align='right')

    drawRect(30, 100, app.width-60, 100, border='black', borderWidth=2, fill=rgb(175, 225, 175))

    # Display user's inventory
    drawLabel("Inventory:", 40, 115, size=15, align='left')
    inventory_y = 135
    i = 1
    for item in app.displayed:
        drawLabel(f'{i}. {item} x{app.inventory.count(item)}', 45, inventory_y, align='left')
        inventory_y += 15
        i += 1

    drawRect(30, 225, app.width-60, 450, border='black', borderWidth=2, fill=rgb(255, 255, 224))
    drawLabel("Items for purchase:", 40, 240, size=15, align='left')
    
    # Display items for sale
    x = 50
    y = 260
    for i in range(len(app.item_images)):
        image = app.item_images[i]
        description = app.item_descriptions[i]
        cost = app.item_costs[i]

        # Display item image, description, and cost
        drawImage(image, x, y, width=80, height=80)
        drawLabel(description, x + 100, y+10, size=14, align='left')
        drawLabel(f"Cost: ${cost}", x + 100, y + 40, size=14, align='left')

        # Check if user can afford item and add a purchase button
        if app.money >= cost:
            if app.active_item == i:
                drawRect(x + 300, y + 50, 80, 30, fill='green')
                drawLabel("Purchase", x + 340, y + 65, size=14)
            else:
                drawRect(x + 300, y + 50, 80, 30, fill='white')
                drawLabel("Purchase", x + 340, y + 65, size=14, align='center')
        else:
            drawRect(x + 250, y + 50, 130, 30, fill='lightGray')
            drawLabel("Not enough money", x + 250+130/2, y + 65, size=14, fill='red')
        
        y += 100

def helper(mouseX, mouseY, x, y, width, height):
    if x <= mouseX <= x + width and y <= mouseY <= y + height:
        return True
    return False

def onMousePress(app, mouseX, mouseY):
    x = 50
    y = 260
    for i in range(len(app.item_images)):
        cost = app.item_costs[i]
        if app.money >= cost:
            if helper(mouseX, mouseY, x + 300, y + 50, 80, 30):
                app.money -= cost
                app.inventory.append(app.item_names[i].split('.')[0])
                app.active_item = i    
                app.displayed = set(app.inventory)    
        y += 100

def main():
    runApp()

main()
