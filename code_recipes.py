import json
import os
import random
import time
import requests
import tkinter
from tkinter import *
from tkinter import scrolledtext
from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
    }
    project_data_dict = {}
    iteration_count = 12
    print(f"Interations = #{iteration_count}")

    for item in range(1, 13):
        req = requests.get(url + f"page/{item}", headers)

        folder_name = f"data/data_{item}"

        if os.path.exists(folder_name):
            print("Folder exists!")
        else:
            os.mkdir(folder_name)

        with open(f"{folder_name}/recipes_{item}.html", "w", encoding="UTF-8") as file:
            file.write(req.text)

        with open(f"{folder_name}/recipes_{item}.html", encoding="UTF-8") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        recipes = soup.find_all("div", class_="col-sm-6 col-md-4 recipe-col mb-3")

        project_urls = []
        for recipe in recipes:
            project_url = recipe.find("div", class_="card recipe-card w-100 h-100 mobile-shadow").find("a").get("href")
            project_urls.append(project_url)

        for project_url in project_urls:
            req = requests.get(project_url, headers)
            project_name = project_url.split("/")[-2]

            with open(f"{folder_name}/{project_name}.html", "w", encoding="UTF-8") as file:
                file.write(req.text)

            with open(f"{folder_name}/{project_name}.html", encoding="UTF-8") as file:
                src = file.read()

            soup = BeautifulSoup(src, "lxml")
            project_data = soup.find("article", class_="recipe-page py-2")

            try:
                project_title = project_data.find("div", class_="col-md-8 pr-md-2").find("h1").text
            except Exception:
                project_title = "No recipe title"

            try:
                ingredients = project_data.find_all("div", class_="col-md-4 col-sm-6")
                project_ingredients = []
                for ingredient in ingredients:
                    temp_ingr = ingredient.find("a").get("title")
                    project_ingredients.append(temp_ingr)
            except Exception:
                project_ingredients = ["No ingredients in recipe"]

            project_data_dict.update({project_title: project_ingredients})

        iteration_count -= 1
        print(f"Interation #{item} completed, #{iteration_count} iterations left")
        if iteration_count == 0:
            print("The end of data collection")
        time.sleep(random.randrange(2, 4))
    with open("data/projects_data.json", "a", encoding="UTF-8") as file:
        json.dump(project_data_dict, file, indent=4, ensure_ascii=False)


def clicked():
    user_input = set(txt.get().split(", "))
    window2 = Tk()
    window2.title("РЕЦЕПТ(Ы)")
    window2.geometry('900x800')
    window2['bg'] = 'antiquewhite'
    txt2 = scrolledtext.ScrolledText(window2, width=90, height=40)
    txt2.grid(column=0, row=2)
    btn3 = Button(window2, text=f'У вас есть {", ".join(user_input)}\nВы можете приготовить:',font=('TkHeadingFont', 15), fg='indianred', bg='antiquewhite', highlightthickness=0)
    btn3.grid(column=0, row=1)
    item = 1
    for k, v in all_recipes.items():
        if user_input <= set(v):
            txt2.insert(INSERT, f"#{item}: {k}\n")
            txt2.insert(INSERT, f"Дополнительно понадобятся: \n{', '.join(set(v).difference(user_input))}\n\n")
            item += 1
    if item == 1:
        txt2.insert(INSERT, f"В нашей базе нет ни одного рецепта с использованием этих ингредиентов :(")


# get_data('https://art-lunch.ru/all-recipes/')
# строка незакоментирована, когда в первый раз запускаем код, он собирает данные и сохраняет в файл
# при последующем использовании - строка комментируется, парсинг снова выполнять не нужно
with open("data/projects_data.json", "r", encoding="UTF-8") as file:
    all_recipes = json.load(file)
builders = "Грибанова Диана\nПереяславцева Ирина\nСавина Арина\nТокунова Полина"

window = Tk()
window.title("КНИГА РЕЦЕПТОВ")
window.geometry('1350x1000')

lbl = Label(window, text="Введите ингредиенты: ", font=('TkHeadingFont', 18), fg='indianred')
lbl.grid(column=0, row=0)
txt = Entry(window, width=90)
txt.grid(column=0, row=1)

btn = Button(window, text='Найти рецепт!', command=clicked, font=('TkHeadingFont', 15), fg='indianred', bg='blanchedalmond')
btn.grid(column=1, row=1)
window['bg'] = 'antiquewhite'
lbl['bg'] = 'antiquewhite'
btn2 = Button(text=f"Более подробный рецепт можно найти на сайте: Арт-Ланч\n\nРазработчики:\n{builders}", font=('TkHeadingFont', 11), bg='antiquewhite')
btn2.grid(row=0, column=1, rowspan=5, columnspan=5)

canvas = tkinter.Canvas(window, height=670, width=860, bg='antiquewhite', highlightthickness=0)
img = tkinter.PhotoImage(file="culinary.png")
image = canvas.create_image(90, 50, anchor='nw', image=img)
canvas.grid(row=2, column=0)

txt.focus()
window.mainloop()
