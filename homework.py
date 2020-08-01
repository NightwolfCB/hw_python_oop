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
        self.currency = currency
        if currency == 'rub':
            currency_name = "руб"
            if cash_remained > 0:
                return f'На сегодня осталось {cash_remained} {currency_name}'
            elif cash_remained == 0:
                return f'Денег нет, держись'
            else:
                cash_remained_abs = abs(cash_remained)
                return f'Денег нет, держись: твой долг - {cash_remained_abs} {currency_name}'

        elif currency == 'usd':
            cash_remained = round(cash_remained / (self.USD_RATE), 2)
            currency_name = "USD"
            if cash_remained > 0:
                return f'На сегодня осталось {cash_remained} {currency_name}'
            elif cash_remained == 0:
                return f'Денег нет, держись'
            else:
                cash_remained_abs = abs(cash_remained)
                return f'Денег нет, держись: твой долг - {cash_remained_abs} {currency_name}'
 
        elif currency == 'eur':
            cash_remained = round(cash_remained / (self.EURO_RATE), 2)
            currency_name = "Euro"
            if cash_remained > 0:
                return f'На сегодня осталось {cash_remained} {currency_name}'
            elif cash_remained == 0:
                return f'Денег нет, держись'
            else:
                cash_remained_abs = abs(cash_remained)
                return f'Денег нет, держись: твой долг - {cash_remained_abs} {currency_name}'

   
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained = self.limit - self.get_today_stats()
        if calories_remained > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_remained} кКал'
        return f'Хватит есть!'


cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment="кофе"))
cash_calculator.add_record(Record(amount=1000, comment="Серёге за обед"))
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="31.07.2020"))
print(cash_calculator.get_today_cash_remained("rub"))
