import tkinter
sirka = int(input('šírka plochy: '))

canvas = tkinter.Canvas(bg='white', width=sirka)
canvas.pack()

x = 5
a = 10
while x + a < sirka:
    canvas.create_rectangle(x, 200, x+a, 200-a)
    x = x + a
    a = a + 10
# príkazy za cyklom
# zobrazenie pracovneho ramca
canvas.mainloop()
