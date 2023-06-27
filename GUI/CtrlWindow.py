import tkinter as tk
from socket import *

from constants import *
from GUI.CtrlPage1 import *
from GUI.CtrlPage2 import *
from GUI.AttackWindow import *

class CtrlWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        self.title("Control Panel")
        self.geometry("300x50")
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight()
        self.geometry(f"+{int(2*ws/5)}+{int(hs/9)}")
        container.pack()
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind(("127.0.0.1", GUI_PORT))
        self.attack_win =None
        self.export_win =None
        self.frames = {}
        for F in (CtrlPage1, CtrlPage2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_page(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def wait_for_confirmation(self):
        counter = 0
        print("Intializing modules...")
        while counter<2:
            msg = self.socket.recv(1024) 
            if (msg == POWERENGINE_READY):
                print("Power Engine ready!")
                counter += 1
            elif (msg == PLOTSERVER_READY):
                print("Plot Server ready!")
                counter += 1
        self.show_page(CtrlPage1)

    def on_closing(self, procs):


        for p in procs:
            if p.is_alive():
                self.socket.sendto(KILL_SIM, (UDP_IP, POWER_PORT))
                p.kill()
        
        if (not (self.attack_win ==None)):
            try:
                self.attack_win.destroy()
            except tk.TclError:
                pass

        if not (self.export_win ==None):
            try:
                self.export_win.destroy()
            except tk.TclError:
                pass
        self.destroy()
