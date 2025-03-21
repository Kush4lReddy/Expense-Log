import purchase
import manageCSV


class PurchaseManager:
    def __init__(self):
            self.csv_manager = manageCSV.ManageCSV()
            self.purchase = purchase


    def add(self):
        name = input("Enter purchase name: ")
        price = float(input("Enter price: "))
        date_of_purchase = input("Enter date of purchase (DD-MM-YYYY): ")
        usage_rate = float(input("Enter the avg no of days you use it every 10 days: "))

        purchase = self.purchase.Purchase(name, price, date_of_purchase, usage_rate)
        self.csv_manager.add_purchase(purchase)
        print("Purchase Added Successfully!")


    def delete(self):
        name = input("Enter purchase name: ")
        self.csv_manager.delete(name)
        print("Purchase Deleted Successfully!")
        

    def load(self):
        self.csv_manager.printCSV()


    def main(self):

        while True:
            print("\nPurchase Tracker")
            print("1. Add Purchase")
            print("2. Delete Purchases")
            print("3. View Purchases")
            print("4. Exit")
            print()
            choice = 0
            try:
                choice = int(input("Enter your choice: ")) # input in float
                if choice < 0:  
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")  # retry
            
            if choice == 1:
                self.add()
            
            elif choice == 2:
                self.delete()

            elif choice == 3:
                self.load()

            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice, try again!")


if __name__ == "__main__":
    pm = PurchaseManager()  # Create an instance
    pm.main()