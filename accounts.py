import datetime
import pytz


class Account:
    """Simple class account with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self.name)
        self._show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your account balance")
        self._show_balance()

    def _show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "Deposited"
            else:
                tran_type = "Withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was: {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim._show_balance()

    tim.deposit(1000)
    #tim.show_balance()
    tim.withdraw(500)
    #tim.show_balance()
    
    tim.withdraw(2000)
    tim.show_transactions()

    steph = Account("Steph", 800)
    steph.__balance = 200
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    steph._show_balance()
    print(steph.__dict__)
    steph._Account__balance = 40
    steph._show_balance()
