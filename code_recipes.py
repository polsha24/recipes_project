import json
import os
import random
import time
import requests
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
    # with open("data/projects_data.txt", "w", encoding="UTF-8") as file:
    #     for k, v in project_data_dict.items():
    #         file.write(f"{k}: {', '.join(v)}\n")
    with open("data/projects_data.json", "a", encoding="UTF-8") as file:
        json.dump(project_data_dict, file, indent=4, ensure_ascii=False)

    #     project_data_dict.append({"Name": project_title, "Ingredients": project_ingredients, "Link": project_url})
    # with open("data/projects_data.txt", "w", encoding="UTF-8") as file:
    #     for i in project_data_dict:
    #         for k, v in i.items():
    #             file.write(f"{k}: {v}; ")
    #         file.write("\n")


# get_data('https://art-lunch.ru/all-recipes/')

# print(all_recipes)
# all_recipes = {}
with open("data/projects_data.json", "r", encoding="UTF-8") as file:
    all_recipes = json.load(file)

user_input = set(input("Введите ингредиенты через запятую:\n").split(", "))
item = 1
for k, v in all_recipes.items():
    if user_input <= set(v):
        print(f"#{item}: {k}")
        print(f"Дополнительно понадобятся: \n{', '.join(set(v).difference(user_input))}\n")
        item += 1
if item == 1:
    print("В нашей базе нет ни одного рецепта с использованием этих ингредиентов :(")
