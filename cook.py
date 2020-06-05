def my_list(cook_book):
    with open (cook_book, 'r', encoding='utf-8') as string:
        cook_book = {}
        def my_list():
            dish = string.readline().strip()
            if dish:
                cook_book[dish] = []
                ingredient_number = string.readline()
                for line in range(int(ingredient_number)):
                    ingredient = string.readline().strip().split(' | ')
                    diction = {'Ингридиенты': ingredient[0], 'Количество': ingredient[1], 'Исчисление': ingredient[2]}
                    cook_book[dish].append(diction)
            else:
                return(cook_book)
            string.readline()
            my_list()
        my_list()
    return(cook_book)

def dishes(test, count):
    cook_book = my_list('cook_book.txt')
    shop_list = {}
    for dish in test:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['Ингридиенты'] not in shop_list:
                    shop_list[ingredient['Ингридиенты']] = {'Исчисление': ingredient['Исчисление'], 'Количество': (int(ingredient['Количество'])* count)}
                else:
                    shop_list[ingredient['Ингридиенты']]['Количество'] += (int(ingredient['Количество'])* count)
    return(shop_list)

print(my_list('cook_book.txt'))
print(dishes(['Омлет', 'Фахитос'], 10))
