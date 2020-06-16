# import numpy as np
# from PIL import ImageGrab
# import cv2
# import time
# import pyautogui

# last_time = time.time()

# while(True):
#   screen = ImageGrab.grab(bbox=(0, 40, 1200, 1200))
 
#   print('Loop took {} seconds'.format(time.time() - last_time))
#   last_time = time.time()
#   cv2.imshow('window', cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY))

#   if cv2.waitKey(25) & 0xFF == ord('q'):
#     cv2.destroyAllWindows()
#     break


import numpy as np
import cv2
import glob
# from moviepy.editor import VideoFileClip
from mss import mss
from PIL import Image
import time
import pyautogui

color = (0, 255, 0) # bounding box color.

# This defines the area on the screen.
mon = {'top' : 200, 'left' : 100, 'width' : 1800, 'height' : 800}
sct = mss()
previous_time = 0

for i in list(range(2))[::-1]:
  print(i+1)
  time.sleep(1)

pyautogui.keyDown('down')
time.sleep(1)
pyautogui.keyUp('down')
time.sleep(1)

pyautogui.keyDown('up')
time.sleep(1)
pyautogui.keyUp('up')

while True:
    screen = sct.grab(mon)
    frame = Image.frombytes( 'RGB', (screen.width, screen.height), screen.rgb )
    frame = np.array(frame)
    frame = frame[ ::2, ::2, : ] # can be used to downgrade the input
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow ('frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    txt1 = 'fps: %.1f' % ( 1./( time.time() - previous_time ))
    previous_time = time.time()
    print(txt1)