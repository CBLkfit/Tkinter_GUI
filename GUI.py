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
        master.title(Lung_nodule)
        master.geometry("1800x1600")
        frame0 = Frame(master) #创建一个框架
        frame0.pack()

        bt0 = Button(frame0, text='File', highlightbackground='#3E4149', command=self.loadData)
        bt1 = Button(frame0, text='P1', command=self.Segmentation)
        bt2 = Button(frame0, text='P2', command=self.Detection)
        bt3 = Button(frame0, text='CLEAR ALL', command=self.ClearAll)

        m1 = Label(frame0, text='Please select the image file.')
        m2 = Label(frame0, text='Do the Segmentation!')
        m3 = Label(frame0, text='Do the detection!')

        bt0.grid(row=1, ipadx=20, ipady=5)
        bt1.grid(row=2, ipadx=20)
        bt2.grid(row=3, ipadx=20)
        bt3.grid(row=1, column=30, ipadx=20, ipady=5)

        m1.grid(row=1, column=5, sticky=W)
        m2.grid(row=2, column=5, sticky=W)
        m3.grid(row=3, column=5, sticky=W)

    def loadData(self):
        ftypes = [('Image Files', '*.tif *.jpg *.png')]
        fd = tkFileDialog.Open(self.master, filetypes=ftypes)
        filename = fd.show()
        img = PIL.Image.open(filename)
        img.thumbnail((400,400),PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(img)
        self.label0 = Label(image=photo)
        self.label0.image = photo #keep a reference
        self.label0.pack(side=LEFT)
      
    def Segmentation(self):
        video_name = '1.mp4'
        self.video = imageio.get_reader(video_name)
        self.vedio_show = Label()
        self.vedio_show.pack(side=LEFT)
        thread = threading.Thread(target=self.stream, args=(self.vedio_show,))
        thread.setDaemon(True)
        thread.start()
        print('segment!')

    def Detection(self):
        img = PIL.Image.open('309_1.tif')
        #img.thumbnail((450,450),Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(img)
        self.label2 = Label(image=photo)
        self.label2.image = photo #keep a reference
        self.label2.pack(side=LEFT)
        print('detect!')

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
