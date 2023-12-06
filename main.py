import tkinter as tk

class MyCalculator:
    def __init__(self):
        height = 6
        width = 12
        xOffet = 100
        yOffset = 100
        fontSize = 10

        self.root = tk.Tk()
        self.root.geometry("400x600")
        self.root.title("Epic gaming calculator")

        #Row0
        self.label = tk.Label(self.root, text="whats up Beijing",
                              font=('Comic Sans MS', 10))
        self.label.place(x=xOffet*0, y=yOffset*0)

        #Row1
        self.button = tk.Button(self.root, text="C",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*0, y=yOffset*1)
        self.button = tk.Button(self.root, text="()",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*1, y=yOffset*1)
        self.button = tk.Button(self.root, text="%",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*2, y=yOffset*1)
        self.button = tk.Button(self.root, text="/",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*3, y=yOffset*1)

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
        self.button = tk.Button(self.root, text="5",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*1, y=yOffset*3)
        self.button = tk.Button(self.root, text="6",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*2, y=yOffset*3)
        self.button = tk.Button(self.root, text="-",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*3, y=yOffset*3)

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
        self.button = tk.Button(self.root, text=".",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*2, y=yOffset*5)
        self.button = tk.Button(self.root, text="=",
                                font=('Arial', fontSize),
                                justify="center",
                                width=width, height=height)
        self.button.place(x=xOffet*3, y=yOffset*5)

        self.root.mainloop()

MyCalculator()