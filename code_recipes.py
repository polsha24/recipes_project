import requests
from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
    }

    # req = requests.get(url, headers)
    # print(req.text)
    # with open("recipes.html", "w", encoding="UTF-8") as file:
    #     file.write(req.text)

    with open("recipes.html", encoding="UTF-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    recipes = soup.find_all("div", class_="col-sm-6 col-md-4 recipe-col mb-3")

    project_urls = []
    for recipe in recipes:
        project_url = recipe.find("div", class_="card recipe-card w-100 h-100 mobile-shadow").find("a").get("href")
        project_urls.append(project_url)

    for project_url in project_urls[0:1]:
        req = requests.get(project_url, headers)
        project_name = project_url.split("/")[-2]

        with open(f"data/{project_name}.html", "w", encoding="UTF-8") as file:
            file.write(req.text)

        with open(f"data/{project_name}.html", encoding="UTF-8") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        project_data = soup.find("article", class_="recipe-page py-2")

        try:
            project_title = project_data.find("div", class_="col-md-8 pr-md-2").find("h1").text
            print(project_title)
        except Exception:
            project_title = "No recipe title"

        ingredients = project_data.find_all("div", class_="col-md-4 col-sm-6")
        project_ingredients = []
        for ingredient in ingredients:
            temp_ingr = ingredient.find("a").get("title")
            project_ingredients.append(temp_ingr)
        print(*project_ingredients)
get_data('https://art-lunch.ru/all-recipes/')



