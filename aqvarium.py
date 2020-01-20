from tkinter import *
from random import *


class Akvarium:
    window = Tk()
    window.title('Работа с canvas')
    X_A = 50
    Y_A = 250
    XM_A = 50+500
    YM_A = 250+300
    canvas = Canvas(window, width=700, height=600, bg="gray")
    Poz_fish = []
    var = []
    fill_a = 'grey'
    colors = ('aqua', 'fuchsia', 'green', 'maroon', 'orange',
                  'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime',)

    def __init__(self):
        self.canvas.create_rectangle(self.X_A, self.Y_A, self.XM_A, self.YM_A, fill=self.fill_a, outline="blue")
        self.canvas.pack()

    def draw(self, fillfish, X, Y, Z):
        self.var.append(self.canvas.create_rectangle(self.X_A + X, self.Y_A + Y, self.X_A + X + Z, self.Y_A + Y + 10, fill=fillfish,outline="blue"))

    def add_fish(self, fillfish1, X1, Y1, Z1):
        self.Poz_fish.append(fillfish1 + ' ' + str(X1) + ' ' + str(Y1) + ' ' + str(Z1))
        self.draw(fillfish1, X1, Y1, Z1)

    def random_fish(self, moder):
        mode = moder
        if (int(mode[1]) > self.X_A) and (int(mode[1]) < self.XM_A):
            mode[1] = str(randint(int(mode[1])-10, int(mode[1])+10))
        if (int(mode[2]) > self.Y_A) and (int(mode[2]) < self.YM_A):
            mode[2] = str(randint(int(mode[2])-1, int(mode[2])+2))
        return mode

    def swimming_fish(self):
        self.canvas.create_rectangle(self.X_A, self.Y_A, self.XM_A, self.YM_A, fill=self.fill_a, outline="blue")
        for x in range(len(self.Poz_fish)):
            s = self.Poz_fish[x]
            s = s.split()
            s = self.random_fish(s)
            self.draw(s[0], int(s[1]), int(s[2]), int(s[3]))
            self.Poz_fish[x] = (s[0] + ' ' + s[1] + ' ' + s[2] + ' ' + s[3])
        self.fill_a = self.colors[randint(1, 12)]
        self.window.update()

    def close(self):
        self.window.mainloop()


A_K = Akvarium()
A_K.fill_a = 'red'
for i in range(1000):
    A_K.add_fish(A_K.colors[randint(1, 12)], randint(1, 500), randint(1, 300), randint(10, 20))
for i in range(100):
    A_K.swimming_fish()
# for i in range(10):
#     A_K.window.coords(A_K.var[i], 0, 0, 75, 25)
# print(A_K.var)
A_K.close()
