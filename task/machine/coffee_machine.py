espresso_beans = 16
espresso_water = 250
espresso_milk = 0
espresso_cost = 4

latte_beans = 20
latte_water = 350
latte_milk = 75
latte_cost = 7

cappuccino_beans = 12
cappuccino_water = 200
cappuccino_milk = 100
cappuccino_cost = 6


class CoffeeMachine:
    def __init__(self, status_water, status_milk, status_beans, status_cups, status_money):
        self.status_water = status_water
        self.status_milk = status_milk
        self.status_beans = status_beans
        self.status_cups = status_cups
        self.status_money = status_money

    class Coffee:
        def __init__(self, beans, water, milk, cup, cost):
            self.beans = beans
            self.water = water
            self.milk = milk
            self.cup = cup
            self.cost = cost

    espresso = Coffee(espresso_beans, espresso_water, espresso_milk, 1, espresso_cost)
    latte = Coffee(latte_beans, latte_water, latte_milk, 1, latte_cost)
    cappuccino = Coffee(cappuccino_beans, cappuccino_water, cappuccino_milk, 1, cappuccino_cost)

    def machine_sell(self):
        try:
            user_command = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n'))
            print('')
            if user_command == 1:
                coffee = self.espresso
            elif user_command == 2:
                coffee = self.latte
            elif user_command == 3:
                coffee = self.cappuccino
        except ValueError:
            return

        if self.verify_resources(coffee):
            self.make_coffee(coffee)


    def verify_resources(self, coffee_type):
        machine_par = ['status_water', 'status_beans', 'status_milk', 'status_cups']
        coffee_par = ['water', 'beans', 'milk', 'cup']
        for index in range(0, len(machine_par)):
            if getattr(self, machine_par[index]) < getattr(coffee_type, coffee_par[index]):
                print(f'Sorry, not enough {coffee_par[index]}! \n')
                return False
        else:
            print('I have enough resources, making you a coffee! \n')
            return True


    def make_coffee(self, coffee_type):
        self.status_water -= coffee_type.water
        self.status_beans -= coffee_type.beans
        self.status_milk -= coffee_type.milk
        self.status_cups -= coffee_type.cup
        self.status_money += coffee_type.cost


    def machine_refill(self):
        self.status_water += int(input('Write how many ml of water you want to add: \n'))
        self.status_milk += int(input('Write how many ml of milk you want to add: \n'))
        self.status_beans += int(input('Write how many grams of coffee beans you want to add: \n'))
        self.status_cups += int(input('Write how many disposable cups of coffee you want to add: \n'))


    def machine_profit(self):
        print(f'I gave you ${self.status_money}')
        print('')
        self.status_money = 0


    def machine_show(self):
        print("The coffee machine has:")
        print(f'{self.status_water} ml of water')
        print(f'{self.status_milk} ml of milk')
        print(f'{self.status_beans} g of coffee beans')
        print(f'{self.status_cups} disposable cups')
        print(f'${self.status_money} of money')
        print('')

    def Main_on(self):
        valid_commands = ['buy', 'fill', 'take', 'remaining', 'exit']
        while True:
            user_command = input('Write action(buy, fill, take, remaining, exit): \n')
            print('')
            if user_command in valid_commands:
                if user_command == 'buy':
                    self.machine_sell()
                elif user_command == 'fill':
                    self.machine_refill()
                elif user_command == 'take':
                    self.machine_profit()
                elif user_command == 'remaining':
                    self.machine_show()
                else:
                    break
            else:
                print('Invalid Option \n')



# Main
# =============

def main():
    my_coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    my_coffee_machine.Main_on()


if __name__ == "__main__":
    main()
