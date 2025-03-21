import csv
import os
import pandas
import purchase

class ManageCSV:

    def __init__(self, filename='purchase.csv'):
        self.filename = filename
        self.header = ['Name','Price','Date of Purchase','Usage Rate','Days Owned','Approx Cost per Day (usage rate)','Cost per Day']

        if not os.path.exists(self.filename):
            self.create_csv()
    

    def create_csv(self):
        self.filename
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.header)


    def add_purchase(self, purchase: purchase.Purchase):
        """Adds a purchase to the CSV file."""
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                purchase.name,
                purchase.price,
                purchase.date_of_purchase.strftime("%d-%m-%Y"),
                purchase.usage_rate,
                purchase.days_owned_,
                purchase.cost_per_day_usage_rate_,
                purchase.cost_per_day_
            ])
    

    def delete(self, name: str): 
        """Deletes a purchase based on the name."""
        with open(self.filename, 'r', newline='') as file:
            reader = csv.reader(file)
            newList = []

            for row in reader:
                if row[0] != name:
                    newList.append(row)

        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(newList)


    def printCSV(self): 
        csvFile = pandas.read_csv(self.filename)
        print(csvFile)



    