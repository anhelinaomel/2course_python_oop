# Pizzeria offers pizza-of-the-day for business lunch. The type of pizza-of-the-day depends on the day of week.
# Also, customers can add extra ingredients to the pizza-of-the-day. Write a program that will form orders from customers.

import datetime

class Pizza:
    extra_ingredients = []
    def addExtraIngredient(self, ingredient):
        self.extra_ingredients.append(ingredient)
    def getIngredients(self):
        return ' '.join(self.ingredients)
    def getExtraIngredients(self):
        return ' '.join(ingredient.getName() for ingredient in self.extra_ingredients)
    def getExtraIngredientsCost(self):
        return sum(ingredient.getIngredientCost() for ingredient in self.extra_ingredients)
    def getTotalCost(self):
        return self.cost + self.getExtraIngredientsCost()
    def getName(self):
        return self.name
    def __str__(self):
        return str(self.getName()) + '\n' + 'Ingredients: ' + str(self.getIngredients()) + '\n' + \
               'Extra Ingredients: ' + self.getExtraIngredients() + '\n' + 'Cost: ' + str(self.getTotalCost())

class Margherita(Pizza):
    name = "Margherita"
    ingredients = ["tomato", "cheese", "olives", "basil"]
    cost = 4.50

class Four_cheeses(Pizza):
    name = "Four cheeses"
    ingredients = ["parmesan", "blue cheese", "cheddar", "mozzarella", "basil", "white sauce"]
    cost = 5.5

class Super_meat(Pizza):
    name = "Super_meat"
    ingredients = ["salami", "ham", "chicken fillet", "mushrooms", "oregano", "BBQ sauce"]
    cost = 11.0

class Pepperoni(Pizza):
    name = "Pepperoni"
    ingredients = ["salami", "mozzarella", "red pepper", "oregano", "tomato sauce"]
    cost = 7.0

class Carbonara(Pizza):
    name = "Carbonara"
    ingredients = ["ham", "mushrooms", "parmesan", "mozzarella", "tomato", "egg", "pepper", "Carbonara sauce"]
    cost = 10.0

class Hawaii(Pizza):
    name = "Hawaii"
    ingredients = ["chicken fillet", "pineapple", "oregano", "mozzarella", "chili pepper", "white sauce"]
    cost = 6.0

class Caprese(Pizza):
    name = "Caprese"
    ingredients = ["feta", "tomato", "sun-dried tomato", "mushroom", "pepper", "basil"]
    cost = 7.2

class Extra_Ingredients:
    def __init__(self):
        pass
    def getIngredientCost(self):
        return self.cost
    def getName(self):
        return self.name

class Cheese(Extra_Ingredients):
    def __init__(self):
        self.name = "Cheese"
        self.cost = 1.0

class Tomato(Extra_Ingredients):
    def __init__(self):
        self.name = "Tomato"
        self.cost = 0.7

class Bacon(Extra_Ingredients):
    def __init__(self):
        self.name = "Bacon"
        self.cost = 2.0

class Mushroom(Extra_Ingredients):
    def __init__(self):
        self.name = "Mushrooms"
        self.cost = 1.8

today = datetime.date.today().weekday()

pizza_day = [Margherita(), Pepperoni(), Carbonara(), Hawaii(),
             Four_cheeses(), Caprese(), Super_meat()]

components = [Cheese(), Tomato(), Bacon(), Mushroom()]

class Order:
    def __init__(self, name = "", surname = "", amount = 0, pizza = []):
        self.name = name
        self.surname = surname
        self.amount = amount
        self.pizza = pizza

order = Order()

while True:
    answer = input("""\nEnter:
    1 - to buy pizza of the day
    2 - to see current order
    3 - to quit\n""")
    if answer == "1":
        print(f'Pizza of the day: {pizza_day[today].getName()}')
        print(f'Ingredients: {pizza_day[today].getIngredients()}')
        print(f'Cost: {pizza_day[today].getTotalCost()}')
        purchase = input('Buy pizza? yes/no\n')
        if purchase == "yes":
            order.pizza = pizza_day[today]
            order.name = input("Enter first name: ")
            order.surname = input("Enter last name: ")
            extra = input("Would you like to put extra ingredients? yes/no\n")
            if extra == "yes":
                choose_extra = input("""Choose extra ingredients(for example: 1 2 3):
                1 - Cheese
                2 - Tomato
                3 - Bacon
                4 - Mushroom\n""")
                # splitting the string into list of extra ingredients:
                choose_extra = list(map(int, choose_extra.split()))
                for ingredient in choose_extra:
                    print(f'Test ingredient {ingredient}')
                    order.pizza.addExtraIngredient(components[ingredient - 1])
            order.amount = input("How many such pizzas you want?\n")
            print(f'Total cost is: {order.pizza.getTotalCost() * int(order.amount)}')
            print("Thank you for your order!")
        elif purchase == "no":
            continue
        else:
            print("Input error!")
    elif answer == "2":
        if order.amount == 0:
            print('You have not ordered any pizza!')
        else:
            print(f'You have ordered {order.amount} {"pizza" if order.amount == 1 else "pizzas"} with the following parameters:\n{order.pizza.__str__()}')
    elif answer == "3":
        break
    else:
        print("Input error!")
