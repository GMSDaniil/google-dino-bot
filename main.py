import pyautogui
from PIL import Image
import keyboard
import time
import math

x,y,w,h = 50 , 300, 1900, 500
jump_time = None
diff = 0
y_search_1, y_search_2 = 364, 328
x_1, x_2 = 400, 415
y_search_bird = 304


while True:
    if keyboard.is_pressed('p'):
        break

while True:
    if keyboard.is_pressed('q'):
        break

    img = pyautogui.screenshot(region=(x,y,w,h))
    img.save('dino.jpg')
    pil_img = Image.open('dino.jpg')
    
    px = pil_img.load()
    
    bg_color = px[0,499]
    for i in range(x_1, x_2):
        if px[i, y_search_1] != bg_color or px[i, y_search_2] != bg_color:
            keyboard.press('space')
            
            if jump_time:
                if math.floor(diff) !=  math.floor(time.time() - jump_time):
                    x_2 = min(x_2+4, 1899)
                    x_1 = max(x_1-1, 370)
                    print('+')
                
                diff = time.time() - jump_time

            jump_time = time.time()
            
            break
            
        elif px[i, y_search_bird] != bg_color:
            keyboard.press('down')
            
            time.sleep(0.4)
            keyboard.release('down')
            break
        
