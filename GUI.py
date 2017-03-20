#-*- coding: UTF-8 -*-
from Tkinter import *
import threading
import PIL.Image
import PIL.ImageTk
import tkFileDialog
import imageio

class Lung_nodule:
    def __init__(self, master):
        self.master = master
        master.title('Lung_nodule')
        master.geometry("1800x1600")
        frame0 = Frame(master) #创建一个框架
        frame0.pack()

        bt0 = Button(frame0, text='Load File', font=("黑体", 15), height=2, width=10, command=self.loadData)
        bt1 = Button(frame0, text='Segment', font=("黑体", 15), command=self.Segmentation, height=2, width=10)
        bt2 = Button(frame0, text='Detect', font=("黑体", 15), command=self.Detection, height=2, width=10)

        m1 = Label(frame0, text='Please select the image file.', font=("黑体", 15))
        m2 = Label(frame0, text='Do the Segmentation!', font=("黑体", 15))
        m3 = Label(frame0, text='Do the detection!', font=("黑体", 15))

        bt3 = Button(frame0, text='CLEAR ALL', font=("黑体", 15), height=2, width=10, command=self.ClearAll)

        bt0.grid(row=0)
        bt1.grid(row=1)
        bt2.grid(row=2)

        m1.grid(row=0, column=5, sticky=W)
        m2.grid(row=1, column=5, sticky=W)
        m3.grid(row=2, column=5, sticky=W)

        bt3.grid(row=0, column=65, sticky=W)

    def loadData(self):
        ftypes = [('Image Files', '*.tif *.jpg *.png')]
        fd = tkFileDialog.Open(self.master, filetypes=ftypes)
        filename = fd.show()
        img = PIL.Image.open(filename)
        img.thumbnail((400,400),PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(img)
        self.label0 = Label(image=photo)
        self.label0.image = photo #keep a reference
        self.label0.place(x=0, y=300)
      
    def Segmentation(self):
        video_name = '1.mp4'
        self.video = imageio.get_reader(video_name)
        self.vedio_show = Label()
        self.vedio_show.place(x=400,y=150)
        thread = threading.Thread(target=self.stream, args=(self.vedio_show,))
        thread.setDaemon(True)
        thread.start()
        print('segment!')

    def Detection(self):
        video_name = '1.mp4'
        self.video = imageio.get_reader(video_name)
        self.label2 = Label()
        self.label2.place(x=900,y=150)
        thread = threading.Thread(target=self.stream, args=(self.label2,))
        thread.setDaemon(True)
        thread.start()
        print('detection!')

    def stream(self,label):
        for image in self.video.iter_data():
            frame_image = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image

    def ClearAll(self):
        self.label0.destroy()
        self.vedio_show.destroy()
        self.label2.destroy()

    
window = Tk() #创建窗口

Lung_nodule(window)

window.mainloop()
