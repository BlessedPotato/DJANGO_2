from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'plov_mem': {
        'укроп, г': 100,
        'картоше4ка, шт': 25,
        'вода, ведро': 1,
        'дрова, охапка': 1,
    }
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def view_recipe(request, dish):
    dish_q = {}
    servings = int(request.GET.get('servings', 1))
    if dish in DATA:
        ingredients = DATA[dish]
        for k, v in ingredients.items():
            dish_q.update({k: v * int(servings)})
    context = {'dish_recipe': dish_q}

    return render(request, 'calculator/index.html', context)

