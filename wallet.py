class Wallet:
    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Додано {amount} грошей. Загальний баланс: {self.balance}")
        else:
            print("Введіть коректну суму для додавання.")

    def spend_money(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Витрачено {amount} грошей. Залишок: {self.balance}")
        else:
            print("Недостатньо грошей на рахунку.")

    def check_balance(self):
        print(f"Поточний баланс: {self.balance}")


def main():
    wallet = Wallet()
    while True:
        print("\nМеню:")
        print("1. Додати гроші")
        print("2. Витратити гроші")
        print("3. Перевірити баланс")
        print("4. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == '1':
            amount = float(input("Введіть суму, яку ви хочете додати: "))
            wallet.add_money(amount)
        elif choice == '2':
            amount = float(input("Введіть суму, яку ви хочете витратити: "))
            wallet.spend_money(amount)
        elif choice == '3':
            wallet.check_balance()
        elif choice == '4':
            print("Дякую за використання! До побачення!")
            break
        else:
            print("Некоректний вибір. Будь ласка, виберіть опцію зі списку.")


if __name__ == "__main__":
    main()
