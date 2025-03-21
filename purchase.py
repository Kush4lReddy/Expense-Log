from datetime import datetime
import csv

class Purchase:
    def __init__(self, name, price, date_of_purchase, usage_rate=5):
        self.name = name
        self.price = price
        self.date_of_purchase = datetime.strptime(date_of_purchase, "%d-%m-%Y")
        self.usage_rate = usage_rate
        self.days_owned_ = self.days_owned()
        self.cost_per_day_usage_rate_ = self.cost_per_day_usage_rate()
        self.cost_per_day_ = self.cost_per_day()

    
    def days_owned(self):
        return (datetime.today() - self.date_of_purchase).days
    
    def cost_per_day(self):
        days = self.days_owned()
        return round(self.price / days, 2) if days > 0 else self.price
    
    def cost_per_day_usage_rate(self):
        days = self.days_owned()
        return ((round(self.price / days, 2)) * 10/self.usage_rate) if days > 0 else self.price

