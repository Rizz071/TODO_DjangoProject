def getMaxOrderNum(TodoDB, TitleDB):
    # определяется запись в БД с максимальным значением поля order_num (поле для сортировки)
    N = 0  # Инициализация порядковой переменной, если БД пуста

    order_nums = []
    for item in TodoDB.objects.filter(title=TitleDB):
        order_nums.append(item.order_num)
        N_max = max(order_nums)
        N_min = min(order_nums)

    print(f'Next order_num will be: {N_max+1}')
    return N_min, N_max

# def get_order_num(dict):
#     for key, value in dict.items():
#         print(key, value)
#
#         if value == '☓':
#             order_num = key
#             return value, order_num
#
#         if value == '↑':
#             order_num = key
#             return value, order_num
#
#         if value == '↓':
#             order_num = key
#             return value, order_num
