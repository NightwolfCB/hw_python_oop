import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        day_sum = 0
        for i in self.records:
            if i.date == dt.date.today():
                day_sum += i.amount
        return day_sum

    def get_week_stats(self):
        week_sum = 0
        now = dt.date.today()
        week_interval = now - dt.timedelta(days=6)
        for i in self.records:
            if week_interval <= i.date <= now:
                week_sum += i.amount
        return week_sum


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CashCalculator(Calculator):
    USD_RATE = float(60.0)
    EURO_RATE = float(70.0)

    def get_today_cash_remained(self, currency):
        cash_remained = self.limit - self.get_today_stats()
        if cash_remained == 0:
            return f'Денег нет, держись'
        currencys = {
            'rub': ['руб', 1],
            'usd': ['USD', CashCalculator.USD_RATE],
            'eur': ['Euro', CashCalculator.EURO_RATE]
            }
        if currency not in currencys:
            return f'Неизвестная валюта'
        if currency in currencys:
            now_cash = cash_remained / currencys[currency][1]
        currency_name = currencys[currency][0]
        if cash_remained > 0:
            return f'На сегодня осталось {now_cash:.2f} {currency_name}'
        now_cash_abs = abs(now_cash)
        message = (
            f'Денег нет, держись: твой долг - '
            f'{now_cash_abs:.2f} {currency_name}'
        )
        return message


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained = self.limit - self.get_today_stats()
        if calories_remained > 0:
            message = (
                f'Сегодня можно съесть что-нибудь ещё, '
                f'но с общей калорийностью не более {calories_remained} кКал'
            )
            return message
        return f'Хватит есть!'
