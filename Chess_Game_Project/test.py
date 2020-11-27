import tkinter as tk

class Gui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.canvas = tk.Canvas(self, width=300, height=200, background='gray')
        self.canvas.create_rectangle(20, 20, 20, 20)
        self.canvas.pack(padx=8, pady=8)


myGui = Gui()
myGui.mainloop()