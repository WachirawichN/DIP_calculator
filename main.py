import tkinter as tk

class MyCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x300")
        self.root.title("Epic gaming calculator")

        #Row0
        self.label = tk.Label(self.root, text="whats up Beijing",
                              font=('Comic Sans MS', 10))
        self.label.place(x=0, y=0)

        #Row1
        self.button = tk.Button(self.root, text="C",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=0, y=50)
        self.button = tk.Button(self.root, text="()",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=50, y=50)
        self.button = tk.Button(self.root, text="%",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=100, y=50)
        self.button = tk.Button(self.root, text="/",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=150, y=50)

        #Row2
        self.button = tk.Button(self.root, text="7",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=0, y=100)
        self.button = tk.Button(self.root, text="8",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=50, y=100)
        self.button = tk.Button(self.root, text="9",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=100, y=100)
        self.button = tk.Button(self.root, text="*",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=150, y=100)

        #Row3
        self.button = tk.Button(self.root, text="4",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=0, y=150)
        self.button = tk.Button(self.root, text="5",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=50, y=150)
        self.button = tk.Button(self.root, text="6",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=100, y=150)
        self.button = tk.Button(self.root, text="-",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=150, y=150)

        #Row4
        self.button = tk.Button(self.root, text="1",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=0, y=200)
        self.button = tk.Button(self.root, text="2",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=50, y=200)
        self.button = tk.Button(self.root, text="3",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=100, y=200)
        self.button = tk.Button(self.root, text="+",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=150, y=200)

        #Row5
        self.button = tk.Button(self.root, text="+/-",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=0, y=250)
        self.button = tk.Button(self.root, text="0",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=50, y=250)
        self.button = tk.Button(self.root, text=".",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=100, y=250)
        self.button = tk.Button(self.root, text="=",
                                font=('Arial', 4),
                                justify="center",
                                width=15, height=10)
        self.button.place(x=150, y=250)

        self.root.mainloop()

MyCalculator()