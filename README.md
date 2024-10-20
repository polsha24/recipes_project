# Приложение “Кулинарная книга”
“Кулинарная книга” это чат-бот-ассистент для приготовления еды. Он помогает выбрать блюдо, которое можно приготовить, на основании введенных пользователем продуктов или категорий блюд, которые пользователь может выбрать из предложенного набора. Бот работает в Telegram, для взаимодействия использует кнопки и текстовые команды в форме названия продуктов.

# Целевая аудитория
Данное приложение предназначено для всех, кто хочет быстро найти идеи для блюд на основе имеющихся ингредиентов или желаемых категорий блюд.

_Важно! Для работы чат-бота необходима мобильная или десктопная версия Telegram._

# Основные функции
1. **Кнопки**
Для взаимодействия с ботом представлены следующие кнопки
- **Завтраки**: Предоставляет пользователю список блюд, отмеченных тэгом “Завтрак”.
- **Салаты**: Предоставляет пользователю список блюд, отмеченных тэгом “Салаты”.
- **Горячее**: Предоставляет пользователю список блюд, отмеченных тэгом “Горячее”.
- **Гарниры**: Предоставляет пользователю список блюд, отмеченных тэгом “Гарниры”.
- **Закуски**: Предоставляет пользователю список блюд, отмеченных тэгом “Закуски”.
- **Десерты**: Предоставляет пользователю список блюд, отмеченных тэгом “Десерты”.
- **Выпечка**: Предоставляет пользователю список блюд, отмеченных тэгом “Выпечка”.
- **Напитки**: Предоставляет пользователю список блюд, отмеченных тэгом “Напитки”.
- **Другое**: Предоставляет пользователю список блюд, отмеченных тэгом “Другое”.
- **Блюда из пищи животного происхождения**: Предоставляет пользователю список блюд, отмеченных тэгом “Блюда из пищи животного происхождения”. 
- **Вывести ещё**: Выводит больше рецептов, соответствующих заданному запросу.

2. **Команды**
Ввод команд в чате происходит через символ косой черты (“/”).
- **/start:** Запускает взаимодействие с ботом и выводит приветственное сообщение с кратким описанием функционала бота.
- **/help:** Выводит ссылку на инструкцию для пользователя.

# Инструкция по использованию
**Запуск бота**
1. Откройте Telegram и введите в поисковой строке @culinary_book_bot.
2. Нажмите кнопку START.

**Выбор блюд по категориям**
1. Выберите необходимую категорию внизу экрана, нажав на кнопку с соответствующим названием. 
2. Для вывода других рецептов, соответствующих тому же запросу, необходимо нажать на кнопку Вывести ещё снизу последнего ответа чат-бота.

**Выбор блюд по введенному продукту**
1. Введите название продукта, который должен быть в рецепте.
2. Для перехода к полной версии рецепта нажмите на ссылку, приведенную внизу описания рецепта.
3. Для вывода других рецептов, соответствующих тому же запросу, необходимо нажать на кнопку Вывести ещё снизу последнего ответа чат-бота.

# Описание файлов .py
- old_code_recipes.py - код предыдущего проекта. Мы решили оставить в этом репозитории, чтобы было видно разницу и можно было судить об улучшениях.
- recipes_parsing.py - код парсинга. С помощью данного кода, мы получили json-файл со списком списков с данными нашего сайта (рецептами блюд) и преобразовали это в датасет в формат csv.
- culinary_book_bot.py - код, который отвечает за работу Telegram чат-бота. Здесь прописан весь функционал бота.
