from datetime import datetime
import matplotlib.pyplot as plt
Expenses={
}
id = 1

def ViewExpenses():
    if not Expenses:
        print("No Expense Added Yet")
    else:    
        for i, n in Expenses.items():
                print(f"ID: {i}")
                print(f"   Name     : {n['Name']}")
                print(f"   Category : {n['Category']}")
                print(f"   Price    : {n['price']}")
                print(f"   Date     : {n['Date']}")
                print("-" * 30)
# Add Expense Ka Function
def AddExpense():
    global id
    Name = input("Enter Name of Expense :")
    Category = input("Enter Category of Expense :")
    try:
        Price = float(input("Enter Price of Expense : "))
    except:
        print("Enter price in digits")    
    try:
        date_input = input("Enter date (DD-MM-YYYY)(OPTIONAL): ")
        if date_input.strip() == "":   
            date = datetime.today() 
        else:    
                date = datetime.strptime(date_input, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format! Please use DD-MM-YYYY") 
        date = datetime.today()
        print("Used todays Date")        
    Expense = {"Name":Name , "Category":Category , "price":Price , "Date":date.date()}     
    Expenses[id] = Expense
    print(f"Expense Added with ID: {id}")
    id += 1

#Delete Expense Ka Option    
def DeleteExpense():
    global id
    ViewExpenses()
    newid = int(input("Enter id to delete that expense :"))
    if newid in Expenses:
       removed =Expenses.pop(newid)
       print(f"Removed Expense with ID {newid}: {removed['Name']} - {removed['price']}")
    else:
        print("Id not found")

#Edit Expense KA Option

def EditExpense():
    global id 
    ViewExpenses()
    newid = int(input("Enter id to Edit that expense :"))
    if newid in Expenses:
        try:
            edit = int(input(f"What you want to edit(1.name/2.category/3.price/4.date): "))
            if edit == 1:
                newname = input(f"Enter new name for {newid} : ")
                Expenses[newid]["Name"] = newname
            elif edit == 2:
                newcategory = input(f"Enter new category for {newid} :")
                Expenses[newid]["Category"] = newcategory
            elif edit == 3:
                try:
                    newprice = float(input(f"Enter new price for {newid} :"))
                    Expenses[newid]["price"] = newprice
                except ValueError:
                    print("Enter price in digits")
            elif edit == 4:
                    try:
                        date_input = input("Enter date (DD-MM-YYYY) or press Enter for today: ")
                        if date_input.strip() == "":
                            newdate = datetime.today()
                        else:
                             newdate = datetime.strptime(date_input, "%d-%m-%Y")
                        Expenses[newid]["Date"] = newdate.date()
                    except ValueError:
                        print("Invalid date format! Please use DD-MM-YYYY") 
                        date = datetime.today()
                        print("Used todays Date")
        except ValueError:
            print("Enter in number")


#Total kitna Expense hoa iska option
def Total():
    while True:
        print("1.Total")
        print("2.Category Wise ")
        print("3.Month Wise:")
        print("4.Exit")
        option = int(input("Enter Option :"))
        if option == 1:       
            ViewExpenses()
            total = sum(exp["price"] for exp in Expenses.values())
            print(f"Total Expense is : {total}")
        elif option == 2:
            CategorywiseTotal()
        elif option == 3:
            MonthWiseTotal()
        elif option == 4:
            break  
        
# Category wise keliye logic
def CategorywiseTotal():
   if not Expenses:
       print("No Expense Added Yet")
   else:    
        CategoryWise = {} 
        for exp in Expenses.values(): 
            category = exp["Category"]
            price = exp["price"]
            CategoryWise[category] = CategoryWise.get(category, 0) + price

        print("\n--- Category Wise Totals ---")
        for cat, total in CategoryWise.items():
            print(f"{cat}: {total}")
        want = input("Want a chart that show category wise distribution?(y/n):").lower()
        if want == "y":
            plt.pie(CategoryWise.values(), labels=CategoryWise.keys(), autopct="%1.1f%%")
            plt.title("Category Wise Expenses")
            plt.show()
        elif want == "n":
            print("Skill Issue")
        else :
            print("Invalid Character. Type y or n")   

        
#Monthly Wise keliye logic
def MonthWiseTotal():
    if not Expenses:
       print("No Expense Added Yet")
    else:
        MonthWise = {}
        YearWise = {}

        for exp in Expenses.values(): 
            date = exp["Date"]
            price = exp["price"]
            key = (date.year, date.month)
            MonthWise[key] = MonthWise.get(key, 0) + price

        print("\n--- Monthly Totals ---")
        for (y, m), total in MonthWise.items():
            print(f"{y}-{m} : {total}")
            YearWise[y] = YearWise.get(y, 0) + total

        print("\n--- Yearly Totals ---")
        for y, total in YearWise.items():
            print(f"{y}: {total}")
        want = input("Want a chart that show monthly/yearly wise distribution?(y/n):").lower()
        if want == "y":
            monthly_yearly = input("Want month wise or year wise (month/year)").lower()
            if monthly_yearly == "month":
                months = [f"{y}-{m}" for (y,m) in MonthWise.keys()]
                totals = list(MonthWise.values())
                plt.bar(months, totals)
                plt.xlabel("Month")
                plt.ylabel("Total Expense")
                plt.title("Month Wise Expense")
                plt.show()

            elif monthly_yearly == "year":
                years = list(YearWise.keys())
                totals = list(YearWise.values())
                plt.bar(years, totals)
                plt.xlabel("Year")
                plt.ylabel("Total Expense")
                plt.title("Year Wise Expense")
                plt.show()
#Expense Tracker    
print("----------------Expense Tracker-------------------")
print("1.View Expenses")
print("2.Add Expense")
print("3.Delete Expense")
print("4.Edit Expense")
print("5.Total")
print("6.Exit")

while True:
    try:
        option = int(input("Enter option number : "))
        if option == 1:
          ViewExpenses()
        elif option == 2:
          AddExpense()
        elif option == 3:
          DeleteExpense()
        elif option == 4:
            EditExpense()
        elif option == 5:
            Total()
        elif option == 6:
           print("Thanks for using")
           break
        else:
            print("Invalid Option")    
    except ValueError:
        print("Enter Number to choose option")   