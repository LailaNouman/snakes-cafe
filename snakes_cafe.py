# welcome = 'Welcome to Snake cafe! \n\nScroll down to see our menu.\n\n'
# exiting = 'You can exit by just writing exit'
# print(welcome)
# print(exiting)
menu = [
    {
        'type': 'Appetizers',
        'food': [
            'Nachos',
            'Frensh fries',
            'Wings',
            'Mozzarela sticks'
        ]
    },
    {
        'type': 'Entrees',
        'food': [
            'Steak',
            'Salmon',
            'Pesto pasta',
            'Fettuccine'
        ]
    },
    {
        'type': 'Dessert',
        'food': [
            'Ice Cream',
            'Chocolate cake',
            'Vanilla',
            'Apple pie'
        ]
    },
    {
        'type': 'Drinks',
        'food': [
            'Coffee',
            'Tea',
            'Soda',
            'Sparkling water'
        ]
    }
]

current_order = []
def get_order(order):
    current_order.append(order)
    order_count = current_order.count(order)
    for i in range(len(menu)):
        if order in menu[i]['food']:
            print(f'**{order_count} order of {order} have been added to your order**')

if __name__ == "__main__":
    welcomig_msg = """ 
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
"""

    print(welcomig_msg)
    for i in range(len(menu)):
        print(menu[i]['type'])
        print('----------')
        for a in menu[i]['food']:
            print(a)
            print('')

print("""
***********************************
** What would you like to order? **
***********************************    
""")

order = input()

while(order != 'quit'):
    get_order(order)
    order = input()

    
