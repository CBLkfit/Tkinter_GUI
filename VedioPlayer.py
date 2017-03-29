#-*- coding: UTF-8 -*-
from collections import deque
import cv2
from PIL import Image, ImageTk
import time

def quit_(root):
    root.destroy()

def update_image(image_label, cam):
    (readsuccessful, f) = cam.read()
    gray_im = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    a = Image.fromarray(gray_im)
    b = ImageTk.PhotoImage(image=a)
    image_label.configure(image=b)
    image_label._image_cache = b  # avoid garbage collection
    root.update()

def update_all(root, image_label, cam):
    update_image(image_label, cam)
    root.after(20, func=lambda: update_all(root, image_label, cam))

def playVedio(root,dir,x0,y0):
    image_label = Label(master=root)# label for the video frame
    image_label.place(x=x0, y=y0)
    cam = cv2.VideoCapture(dir) 
    # setup the update callback
    root.after(0, func=lambda: update_all(root, image_label, cam))