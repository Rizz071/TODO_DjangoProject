def getMaxOrderNum(TodoDB):
    # определяется запись в БД с максимальным значением поля order_num (поле для сортировки)
    N = 0  # Инициализация порядковой переменной, если БД пуста

    order_nums = []
    for item in TodoDB.objects.all():
        order_nums.append(item.order_num)
        N = max(order_nums) + 1

    print(f'Next order_num will be: {N}')
    return N

def get_order_num(dict):
    for key, value in dict.items():
        print(key, value)

        if value == '☓':
            order_num = key
            return value, order_num

        if value == '↑':
            order_num = key
            return value, order_num

        if value == '↓':
            order_num = key
            return value, order_num
