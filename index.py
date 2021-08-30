from tkinter import *
import os
connect = 'nordvpn connect'
disconnect = 'nordvpn disconnect'

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        disconnectButton = Button(self, text="Disconnect",command=lambda: os.system(disconnect))

        # placing the button on my window
        disconnectButton.place(x=80, y=0)

        connectButton = Button(self, text="Connect",command=lambda: os.system(connect))

        # placing the button on my window
        connectButton.place(x=0, y=0)

root = Tk()

#size of the window
root.geometry("180x30")

print("bird")

app = Window(root)
root.mainloop()  

print("yay")