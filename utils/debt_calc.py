from enum import Enum
from typing import List

class Currency(Enum):
    rub = 1
    din = 2
    euro = 3

class User:
    """This class represents user object, contains debt information to other users"""

    _currencyToRub = {Currency.euro: 74.05,
                     Currency.din: 0.62,
                     Currency.rub: 1}

    def __init__(self, name):
        self.name = name
        self.debts = {}

    def __repr__(self):
        return self.name

    def add_debt(self, to, amount, currency = Currency.rub):
        existing_debt = self.debts.get(to,0)

        self.debts[to] = existing_debt + amount * self._currencyToRub[currency]

def record_debt(who, whom, amount, currency = Currency.rub):
    """
    :type whom: User
    :type who: List[User]
    :type amount float
    :type currency Currency
    """
    for u in who:
        u.add_debt(whom,amount,currency)

mark = User("Марк")
vlad = User("Влад")
anton = User("Антон")
matvey = User("Матвей")
ura = User("Юра")

all = [mark,vlad,anton,matvey,ura]
serbia = [mark,vlad,anton,ura]
montenegro = [mark,vlad,anton,matvey]

#Влад
record_debt(serbia, vlad, 1000)
record_debt(serbia, vlad, 300, Currency.din)
record_debt(serbia, vlad, 1612, Currency.din)
record_debt(serbia, vlad, 1925, Currency.din)
record_debt(serbia, vlad, 486, Currency.din)
record_debt([matvey,anton], vlad,60,Currency.euro)
record_debt(montenegro,vlad,10.66/4,Currency.euro)
record_debt(montenegro,vlad,14.11/4,Currency.euro)
record_debt([matvey,anton], vlad,1.93,Currency.euro)
record_debt(montenegro,vlad,1,Currency.euro)
record_debt(montenegro,vlad,3,Currency.euro)
record_debt([mark,anton],vlad,100)
record_debt([mark,matvey],vlad,590)

#Матвей
record_debt([anton,vlad], matvey,2.66,Currency.euro)

#Антон
record_debt([vlad],anton,500)
record_debt(serbia,anton,200,Currency.din)
record_debt([ura,vlad],anton,661,Currency.din)

record_debt(montenegro, anton, 17.325,Currency.euro)
record_debt(montenegro, anton, 10.5,Currency.euro)
record_debt(montenegro, anton, 1.875,Currency.euro)
record_debt(montenegro, anton, 0.5,Currency.euro)
record_debt(montenegro, anton, 8,Currency.euro)
record_debt(montenegro, anton, 2,Currency.euro)
record_debt(montenegro, anton, 10,Currency.euro)
record_debt([vlad], anton, 1.29,Currency.euro)
record_debt([matvey], anton, 0.9,Currency.euro)
record_debt([matvey, vlad], anton, 5.53,Currency.euro)
record_debt(montenegro, anton, 3.75,Currency.euro)
record_debt([matvey, vlad], anton, 3.9,Currency.euro)
record_debt(montenegro, anton, 1.5,Currency.euro)
record_debt([matvey, vlad], anton, 10,Currency.euro)
record_debt([mark], anton, 4,Currency.euro)
record_debt([mark], anton, 2.3,Currency.euro)
record_debt([matvey, vlad], anton, 6.6,Currency.euro)
record_debt(montenegro, anton, 5.25,Currency.euro)
record_debt([mark, vlad], anton, 500)

#Марк
record_debt(serbia, mark, 666, Currency.din)
record_debt(montenegro, mark, 2.94,Currency.euro)
record_debt([vlad], mark, 5,Currency.euro)
record_debt(montenegro, mark, 5.5,Currency.euro)
record_debt([anton, vlad], mark, 2.73,Currency.euro)
record_debt([vlad], mark, 2,Currency.euro)
record_debt(montenegro, mark, 10,Currency.euro)
record_debt([vlad], mark, 50,Currency.euro)
record_debt(montenegro, mark, 13.75,Currency.euro)
record_debt([vlad, anton], mark, 1.66,Currency.euro)
record_debt(montenegro, mark, 15,Currency.euro)
record_debt(montenegro, mark, 2.5 / 4,Currency.euro)
record_debt(montenegro, mark, 12.5,Currency.euro)
record_debt(montenegro, mark, 3,Currency.euro)
record_debt(montenegro, mark, 15.525,Currency.euro)

transactions =  {}

#Бежим по всем пользователям
for u in all:
    #Для каждого пользователя, смотрим его долг
    whom: User
    for whom, u_debt in u.debts.items():
        #Итак, u, должен whom a денег
        whom_debt = whom.debts.get(u,0)
        #Смотрим, сколько whom должен u?
        if u_debt > whom_debt:
            transactions[(u.name,whom.name)] =  u_debt - whom_debt



for k,v in transactions.items():
    print(k[0] + " ->" + k[1] + ":" + str(v))