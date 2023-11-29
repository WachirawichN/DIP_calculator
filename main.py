import tkinter as tk

class MyCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.root.title("Epic gaming calculator")

        #Row0
        self.label = tk.Label(self.root, text="whats up Beijing",
                              font=('Comic Sans MS', 24))
        self.label.place(x=200, y=10)

        #Row1
        self.button = tk.Button(self.root, text="AC",
                                font=('Comic Sans MS', 4))
        self.button.place(x=0, y=50)
        self.button = tk.Button(self.root, text="/",
                                font=('Comic Sans MS', 4))
        self.button.place(x=40, y=50)
        self.button = tk.Button(self.root, text="*",
                                font=('Comic Sans MS', 4))
        self.button.place(x=80, y=50)
        self.button = tk.Button(self.root, text="-",
                                font=('Comic Sans MS', 4))
        self.button.place(x=120, y=50)

        self.root.mainloop()

MyCalculator()