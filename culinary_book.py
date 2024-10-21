import json
import telebot
import random

with open('token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()
bot = telebot.TeleBot(token)

with open("data/recipes.json", "r", encoding="UTF-8") as file:
    all_recipes = json.load(file)
user_states = {}

def get_recipes_by_ingredients(user_input):
    result  = []
    ingredients = set(user_input.lower().split(", "))
    item = 1
    for recipe in all_recipes:
        if set(ingredients) <= set(recipe["Ингредиенты"].lower().split(', ')):
            result.append(f"{recipe['Категория']}\n#{item}: {recipe["Заголовок"]}\nДополнительно понадобятся: "
                          f"\n{', '.join(set(recipe["Ингредиенты"].lower().split(', ')).difference(set(ingredients)))}"
                          f"\n{recipe['Ссылка']}\n\n")
            item += 1
    if item == 1:
        result.append("В нашей базе нет ни одного рецепта с использованием этих ингредиентов :(")
    global recipes_for_user
    recipes_for_user = result
    return result

def send_recipes_page(chat_id):
    user_state = user_states[chat_id]
    recipes = user_state['recipes']
    page = user_state['page']

    per_page = 3
    start_index = page * per_page
    end_index = start_index + per_page

    current_page_recipes = recipes[start_index:end_index]
    if current_page_recipes:
        bot.send_message(chat_id, f"Вот возможные блюда (страница {page + 1}):\n{''.join(current_page_recipes)}")

        if len(recipes) > end_index:
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton("Вывести еще", callback_data=f"next_{chat_id}"))
            bot.send_message(chat_id, "Показать еще?", reply_markup=markup)
    else:
        bot.send_message(chat_id, "Больше рецептов нет.")

def create_category_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Горячее', 'Десерты', 'Закуски', 'Напитки',
               'Блюда из пищи животного происхождения', 'Салаты',
               'Другое', 'Выпечка', 'Гарниры', 'Завтраки')
    return markup

def handle_category(message):
    category = message.text
    recipe_list = []
    for recipe in all_recipes:
        if category in recipe['Категория']:
            recipe_list.append(f"# {recipe["Заголовок"]}\nПонадобятся:"
                               f" \n{recipe["Ингредиенты"]}\n{recipe['Ссылка']}\n\n")
    if recipe_list:
        random_recipes = random.sample(recipe_list, min(5, len(recipe_list)))
        response = f"Рецепты для категории '{category}':\n{''.join(random_recipes)}"
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, f"В категории '{category}' нет рецептов.")



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Введи ингредиенты, или выбери категорию:",
                 reply_markup=create_category_keyboard())

@bot.message_handler(content_types=['text'])
def send_recipes(message):
    user_input = message.text
    if user_input in ['Горячее', 'Десерты', 'Закуски', 'Напитки',
                    'Блюда из пищи животного происхождения', 'Салаты',
                    'Другое', 'Выпечка', 'Гарниры', 'Завтраки']:
        handle_category(message)
    else:
        recipes = get_recipes_by_ingredients(user_input)
        user_states[message.chat.id] = {
            'recipes': recipes,
            'page': 0
        }
        send_recipes_page(message.chat.id)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data.startswith("next_"):
        chat_id = int(call.data.split('_')[1])
        user_states[chat_id]['page'] += 1
        send_recipes_page(chat_id)
        bot.answer_callback_query(call.id)



bot.infinity_polling()
