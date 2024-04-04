from tkinter import Tk, Label, Button
from PIL import Image, ImageDraw, ImageTk


class App:
    def __init__(self, width, height):
        self.tk = Tk()
        self.img = Image.new('RGB', (width, height), 'white')
        self.img_dr = ImageDraw.Draw(self.img)
        self.img_tk = ImageTk.PhotoImage(self.img)
        self.lab = Label(image=self.img_tk)
        self.lab.grid(column=0, row=0)
        self.but = Button(width=10, height=5, command=self.clear, background='white', text='clear', font=100)
        self.but.grid(column=1, row=0)
        self.width = width
        self.height = height
        self.scale = 1

    def get_tk(self):
        return self.tk

    def clear(self):
        self.img_dr.rectangle((0, 0, self.width, self.height), fill='white')
        self.img_tk.paste(self.img)

    def is_fun(self, x, y):
        x -= self.width // 2
        y -= self.height // 2

        if x == 0:
            return False
        if y == 0:
            return False

        x = x / self.scale
        y = y / self.scale

        # y ** 2 + x ** 2 = r ** 2
        # y ** 2 + x ** 2 - r ** 2 = 0
        from math import log, sin, cos, tan

        f = sin(x ** 2 + y ** 2) * cos(x + y) - tan(x * y) ** sin(x * y)

        # if abs(0 - f) <= 1
        if abs(f) <= 1:
            return True

        return False

    def run(self):
        self.img_dr.rectangle((0, 0, self.width, self.height), fill='white')
        self.img_tk.paste(self.img)

        self.scale *= 1.5

        x = 100
        y = 0
        end_x = self.width - 100

        fill = 'black'

        while x < end_x:
            if self.is_fun(x, y):
                # fill = (y % 255, y * 10000, y)
                self.img_dr.rectangle((x, self.height - y, x, self.height - y), fill=fill)

            y += 1
            if y > self.height:
                x = x + 1
                y = 0

        self.img_tk.paste(self.img)
        print('end_painting')
        self.tk.after(1, self.run)


if __name__ == '__main__':
    app = App(750, 600)
    app.run()

    app.get_tk().mainloop()
