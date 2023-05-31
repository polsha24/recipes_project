import tkinter
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk

window = Tk()
window.title("КНИГА РЕЦЕПТОВ")
window.geometry('1350x1000')

lbl = Label(window, text="Введите ингредиенты: ", font=('Courier New', 18), fg='indianred')
lbl.grid(column=0, row=0)
txt = Entry(window, width=90)
txt.grid(column=0, row=1)
ingred = txt.get()


def clicked():
    window2 = Tk()
    window2.title("РЕЦЕПТ(Ы)")
    window2.geometry('1000x1000')
    window2['bg'] = 'antiquewhite'
    txt2 = scrolledtext.ScrolledText(window2, width=60, height=30)
    txt2.grid(column=1, row=3)
    txt2.insert(INSERT, ingred)


btn = Button(window, text='Найти рецепт!', command=clicked, font=('Courier New', 15), fg='indianred', bg='blanchedalmond')
btn.grid(column=1, row=1)
window['bg'] = 'antiquewhite'
lbl['bg'] = 'antiquewhite'
btn2 = Button(text="Более подробный рецепт можно найти на сайте: Арт-Ланч \n Разработчики: \n Грибанова Диана \n Переяславцева Ирина \n Савина Арина \n Токунова Полина", font=('Courier New', 11), bg='antiquewhite')
btn2.grid(row=0, column=1, rowspan=5, columnspan=5)

canvas = tkinter.Canvas(window, height=670, width=860, bg='antiquewhite', highlightthickness=0)
img = tkinter.PhotoImage(file="culinary.png")
image = canvas.create_image(90, 50, anchor='nw', image=img)
canvas.grid(row=2, column=0)

txt.focus()
window.mainloop()
