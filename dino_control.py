import numpy as np
import cv2
import glob
from mss import mss
from PIL import Image
import time
import pyautogui





def detect_rex(frame):
  # All the 6 methods for comparison in a list
  # Note how we are using strings, later on we'll use the eval() function to convert to function
  methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
  sprite = cv2.imread('sprite.png')
  print(sprite.shape)
  roi = sprite[0:100, 1680:1763]

  height, width, channels = roi.shape

  # Get the actual function instead of the string
  method = eval(methods[0])
  # Apply template Matching with the method
  res = cv2.matchTemplate(frame, roi, method)
  # Grab the Max and Min values, plus their locations
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
  # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
  if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
      top_left = min_loc    
  else:
      top_left = max_loc
      
  # Assign the Bottom Right of the rectangle
  bottom_right = (top_left[0] + width, top_left[1] + height)

  # Draw the Red Rectangle
  cv2.rectangle(frame,top_left, bottom_right, 255, 10)

  return frame



def cactus():
  cactus_img = cv2.imread('sprite.png')
  cv2.imshow('frame', cactus_img)

  while True:
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

# cactus()

def screenGrab():
  color = (0, 255, 0) # bounding box color.
  # This defines the area on the screen.
  mon = {'top' : 200, 'left' : 100, 'width' : 1800, 'height' : 800}
  sct = mss()
  previous_time = 0
  while True:
      screen = sct.grab(mon)
      frame = Image.frombytes( 'RGB', (screen.width, screen.height), screen.rgb )
      frame = np.array(frame)
      frame = frame[ ::2, ::2, : ] # can be used to downgrade the input
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      detected_frame = detect_rex(frame)
      cv2.imshow ('frame', detected_frame)
      if cv2.waitKey(25) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          break
      txt1 = 'fps: %.1f' % ( 1./( time.time() - previous_time))
      previous_time = time.time()
      print(txt1)
screenGrab()

def controls():
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
