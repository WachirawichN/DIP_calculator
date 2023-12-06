import tkinter as tk

class MyCalculator:

    title = "MyCalculator"

    def __init__(self):
        height = 6
        width = 12
        xOffet = 100
        yOffset = 100
        fontSize = 10

        self.root = tk.Tk()
        self.root.geometry("400x600")
        self.root.title("Epic gaming calculator")
        self.display = tk.StringVar()

        #Row0
        self.label = tk.Label(self.root, textvariable=self.display,
                              font=('Comic Sans MS', 10))
        self.label.place(x=xOffet*0, y=yOffset*0)

        #Row1
        self.button = tk.Button(self.root, text="C",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*0, y=yOffset*1)
        self.button.bind('<Button-1>', self.event_c)
        self.button = tk.Button(self.root, text="()",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*1, y=yOffset*1)
        self.button.bind('<Button-1>', self.event_wongleb)
        self.button = tk.Button(self.root, text="%",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*2, y=yOffset*1)
        self.button.bind('<Button-1>', self.event_percent)
        self.button = tk.Button(self.root, text="/",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*3, y=yOffset*1)
        self.button.bind('<Button-1>', self.event_divide)

        #Row2
        self.button = tk.Button(self.root, text="7",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*0, y=yOffset*2)
        self.button = tk.Button(self.root, text="8",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*1, y=yOffset*2)
        self.button = tk.Button(self.root, text="9",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*2, y=yOffset*2)
        self.button = tk.Button(self.root, text="*",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*3, y=yOffset*2)

        #Row3
        self.button = tk.Button(self.root, text="4",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*0, y=yOffset*3)
        self.button.bind('<Button-1>', self.event_4)
        self.button = tk.Button(self.root, text="5",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*1, y=yOffset*3)
        self.button.bind('<Button-1>', self.event_5)
        self.button = tk.Button(self.root, text="6",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*2, y=yOffset*3)
        self.button.bind('<Button-1>', self.event_6)
        self.button = tk.Button(self.root, text="-",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*3, y=yOffset*3)
        self.button.bind('<Button-1>', self.event_lob)

        #Row4
        self.button = tk.Button(self.root, text="1",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*0, y=yOffset*4)
        self.button = tk.Button(self.root, text="2",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*1, y=yOffset*4)
        self.button = tk.Button(self.root, text="3",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*2, y=yOffset*4)
        self.button = tk.Button(self.root, text="+",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*3, y=yOffset*4)

        #Row5
        self.button = tk.Button(self.root, text="+/-",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*0, y=yOffset*5)
        self.button = tk.Button(self.root, text="0",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*1, y=yOffset*5)
        self.button.bind('<Button-1>', self.event_zero)
        self.button = tk.Button(self.root, text=".",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*2, y=yOffset*5)
        self.button.bind('<Button-1>', self.event_dot)
        self.button = tk.Button(self.root, text="=",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*3, y=yOffset*5)

        self.root.mainloop()

    def event_c(self, event):
        self.display.set(self.display.get() + "c")
    def event_wongleb(self, event):
        self.display.set(self.display.get() + "()")
    def event_percent(self, event):
        self.display.set(self.display.get() + "%")
    def event_divide(self, event):
        self.display.set(self.display.get() + "/")
    def event_zero(self, event):
        self.display.set(self.display.get() + "0")
    def event_divide(self, event):
        self.display.set(self.display.get() + ".")
    def event_4(self, event):
        self.display.set(self.display.get() + "4")
    def event_5(self, event):
        self.display.set(self.display.get() + "5")
    def event_6(self, event):
        self.display.set(self.display.get() + "6")
    def event_lob(self, event):
        self.display.set(self.display.get() + "-")
    


MyCalculator()