import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(688 ,720):
        for j in range(240 , 295):
            if data[i, j] < 171:
                hit("down")
                return

    for i in range(688 ,770):
        for j in range(295 , 340):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)

       # print(asarray(image))
'''    
        # Draw the rectangle for cactus
        for i in range(688, 800):
            for j in range(298, 340):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(688, 800):
            for j in range(240, 298):
                data[i, j] = 171

        image.show()
        break
'''