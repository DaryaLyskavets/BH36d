# Необходимо выпустить кассовый чек (вернуть строку), в котором будут
# указаны названия товаров, их количество, общая стоимость и общая стоимость с учетом скидок

products = [{'id': '01', 'title': 'milk', 'price': 1.98, 'discount': 1},
            {'id': '02', 'title': 'water', 'price': 1.32, 'discount': 1},
            {'id': '03', 'title': 'potatoes', 'price': 2.5, 'discount': 3},
            {'id': '04', 'title': 'chocolate', 'price': 3.6, 'discount': 5},
            {'id': '05', 'title': 'steak', 'price': 24, 'discount': 12},
            {'id': '06', 'title': 'fish', 'price': 21, 'discount': 15},
            ]
food_basket = [('01', 2), ('03', 5), ('04', 1), ('05', 1)]

def sales_receipt(products, food_basket):
    user_bill = []
    for i in products:
        for j in range(0, 4):
            if food_basket[j][0] == i.get('id'):
                user_bill.append(i.get('title') + ' ' + str(food_basket[j][1]) + ' '+
                                str(i.get('price')*food_basket[j][1]) + ' ' +
                                str(i.get('price')*food_basket[j][1] -
                                i.get('price')*food_basket[j][1]/100*i.get('discount')))
    print(user_bill)

sales_receipt(products,food_basket)