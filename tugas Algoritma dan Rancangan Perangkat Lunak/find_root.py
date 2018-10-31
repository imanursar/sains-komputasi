import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
# import tooltip_oop as tt
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2TkAgg)
from matplotlib.figure import Figure
from skimage import color
from scipy.signal import convolve2d as conv2
from datetime import datetime


class OOP():

    def __init__(self, win, xy1, xy2):
        self.win = win

        #tab ===================================================================
        nb = ttk.Notebook(win, width=1350, height=700)
        nb.pack()

        tab = ttk.Frame(nb)
        nb.add(tab, text='main program')

        #add a window title ====================================================
        self.win.title("Find root")

        #subtab title ==========================================================
        self.frame_tab1_1 = ttk.LabelFrame(tab, text="Input")
        self.frame_tab1_1.grid(column=0, row=0, sticky=tk.N)

        self.frame_tab1_2 = ttk.LabelFrame(tab, text="origin image")
        self.frame_tab1_2.grid(column=1, row=0, sticky=tk.W)

        self.frame_tab1_3 = ttk.LabelFrame(tab, text="edited image")
        self.frame_tab1_3.grid(column=2, row=0, sticky=tk.W)

        self.frame_tab1_4 = ttk.LabelFrame(tab, text="display origin image")
        self.frame_tab1_4.grid(column=1, row=1, sticky=tk.W, columnspan=10)

        self.frame_tab1_5 = ttk.LabelFrame(tab, text="display edited image")
        self.frame_tab1_5.grid(column=2, row=1, sticky=tk.W, columnspan=10)


        #gaussian filter
        #adding block and label
        self.frame_tab1_a1 = ttk.LabelFrame(self.frame_tab1_1, text="gaussian filter")
        self.frame_tab1_a1.grid(column=0, row=3, sticky='WE')

        self.Label_1 = ttk.Label(self.frame_tab1_a1)
        self.Label_1.grid(column=0, row=2, sticky=tk.W)

        #adding dropdown box
        ttk.Label(self.frame_tab1_a1, text="The size gauss filter:").grid(column=0, row=0, padx=15)
        # self.int_gauss = tk.IntVar()
        # self.gauss = ttk.Combobox(self.frame_tab1_a1, width=12, textvariable=self.int_gauss)
        self.gauss = ttk.Combobox(self.frame_tab1_a1, width=12)
        self.gauss['values'] = (1,2,3,4,5,6,7,8,9,10)
        self.gauss.grid(column=0, row=1)
        self.gauss.current(6) #default value

        #adding dropdown box
        ttk.Label(self.frame_tab1_a1, text="sigma:").grid(column=1, row=0)
        self.sigma = ttk.Combobox(self.frame_tab1_a1, width=12)
        self.sigma['values'] = (1,2,3,4,5,6,7,8,9,10)
        self.sigma.grid(column=1, row=1, padx=15)
        self.sigma.current(2) #default value


        # action button
        self.action_1 = ttk.Button(self.frame_tab1_a1, text="gauss Filter", command=self._gauss)
        self.action_1.grid(column=2,row=1)

        #inside origin image ===================================================
        #display image
        fig_1 = plt.figure(figsize=(5,5))
        plt.axis('off')
        # im_1 = plt.imshow(self.image_1)
        fig_1.tight_layout()
        fig_1.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

        self.canvas_1 = FigureCanvasTkAgg(fig_1, master=self.frame_tab1_2)
        self.canvas_1.draw()
        self.canvas_1._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.toolbar = NavigationToolbar2TkAgg(self.canvas_1,self.frame_tab1_4)
        self.toolbar.update()
        self.canvas_1._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=4)

        #inside edited image ===================================================
        #display image
        self.fig_2 = plt.figure(figsize=(5,5))
        plt.axis('off')
        # self.im_2 = plt.imshow(self.image_2)
        self.fig_2.tight_layout()
        self.fig_2.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

        self.canvas_2 = FigureCanvasTkAgg(self.fig_2, master=self.frame_tab1_3)
        self.canvas_2.draw()
        self.canvas_2._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.toolbar = NavigationToolbar2TkAgg(self.canvas_2,self.frame_tab1_5)
        self.toolbar.update()
        self.canvas_2._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=4)

        #adding menu bar =======================================================
        menu = Menu(win, tearoff=0)
        win.config(menu=menu)

        #add menu Item
        fileMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="New")
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=win.destroy)

        helpMenu = Menu(menu, tearoff=0) #tearoff =0 menghilangkan dash line diawal
        menu.add_cascade(label="help", menu=helpMenu)
        helpMenu.add_command(label="About")

    #Button callback ===========================================================
    def _gauss(self):
        self.image_g = color.rgb2gray(self.image_1)
        self.filter_g = self._gauss_filter((int(self.gauss.get()),int(self.gauss.get())),int(self.sigma.get()))
        self.image_gf = conv2(self.image_g, self.filter_g,mode='same')

        self.im_2 = plt.imshow(self.image_gf)
        self.canvas_2.draw()

        self.Label_1.configure(foreground='blue')
        self.Label_1.configure(text="gauss= " + self.gauss.get() + " | sigma= " + self.sigma.get())
        print("gauss= " + self.gauss.get() + " | sigma= " + self.sigma.get())
        self.scr1.insert(tk.INSERT, datetime.now().strftime('%H:%M:%S') + " >> " + "Gaussian filter with parameter: " + '\n')
        self.scr1.insert(tk.INSERT, "\t    " + "The size of gauss filter = " + self.gauss.get() + " | sigma = " + self.sigma.get() + '\n')
        self.scr2.insert(tk.INSERT, datetime.now().strftime('%H:%M:%S') + " >> " + "Gaussian filter with parameter: " + '\n')
        self.scr2.insert(tk.INSERT, "\t    " + "The size of gauss filter = " + self.gauss.get() + " | sigma = " + self.sigma.get() + '\n')


    def _findroot(self):


    def _newton_raphson(self):



root = tk.Tk()
# root.geometry('1366x786')
# root.resizable(width=False, height=False)
# app=FullScreenApp(root)
root.iconbitmap(r'D:\software\python\conda\Anaconda3\DLLs\pyc.ico')

# root.overrideredirect(True)
# root.overrideredirect(False)
root.attributes('-fullscreen',True)
# root.state('zoomed')
# root.bind('<Escape>',lambda e: root.destroy())
main_win = OOP(root,0,1400)
root.mainloop()
