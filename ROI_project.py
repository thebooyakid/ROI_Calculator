class Calculator:

    """
        This program will take unser input in the form of integers or floats, and calculate a return on investment for their property
        The program is set with averages for the user's area if they don't want to go through the whole calculation
    """
    
    def __init__(self, income = 2000, expenses = 1610, cashFlow = 390):
        self.income = income
        self.expenses = expenses
        self.cashFlow = cashFlow

    def giveAverage(self):
        print("\nWelcome to the Return on Investment Calculator")
        print("We're going to ask you some financial questions")
        self.address = input("But first, whats the address of the property we'll be dealing with today? ")
        print("\nWe would like to be as accurate as possilbe, but if you would like, we can quickly give you an average for you area. ")
        avg = input("If you would like to see an average, input 'y' otherwise just hit enter: ")
        if avg.lower() == 'y':
            area = input("Do you live in the 'east' 'west' 'north' or 'south? ")
            if area.lower() == 'north':
                self.income = 2200
                self.expenses = 1800
                self.cashFlow = 400
            elif area.lower() == 'west':
                self.income = 2100
                self.expenses = 1770
                self.cashflow = 330
            elif area.lower() == 'north':
                self.income = 2050
                self.expenses = 1630
                self.cashflow = 320
            elif area.lower() == 'south':
                self.income = 1900
                self.expenses = 1550
                self.cashflow = 350
            else:
                print("We'll just do the national average")    
            print("\nWe will just need to ask you a few questions about your total cash investment to calculate your average. ")
            Calculator.cashOnCash(self)
        else:
            Calculator.userInputIncome(self)

    def userInputIncome(self):
        print("\nPlease answer all questions inputting only numbers")
        rentalIncome = input("\nWhat is your monthly rental income on your property? $")
        miscIncome = input("If you charge any miscellaneous fees on your property (laundry, storage, etc) what is your monthly income from them? $")
        try:
            totalMonthlyIncome = float(rentalIncome) + float(miscIncome)
        except ValueError:
            print("\nOne of your values was not entered as a number.")
            print("We will need to start over to get an accurate calculation")
            Calculator.userInputIncome(self)
        print(f"\nYour total monthly income from the property is ${totalMonthlyIncome}")
        self.income = totalMonthlyIncome
        Calculator.userInputExpenses(self)
    
    def userInputExpenses(self):
        print("\nNow we're going to ask you some questions about your expenses.")
        print("Please remeber to respond using numbers only...")
        mortgage = input("\nHow much do you pay monthly for your mortgage? $")
        tax = input("How much do you pay in monthly taxes? $")
        insurance = input("How much do you pay monthly for insurance? $")
        lawn = input("How much do you pay monthly for lawn care? $")
        response = input("Do you pay for utilities? Please type 'y' for yes, and 'n' for no: ")
        if response.lower() == 'n':
            electric = 0
            water = 0
            sewer = 0
            gas = 0
            otherUtilities = 0
            pass
        elif response.lower() == 'y':
            electric = input("How much is your monthly electric bill? $")
            water = input("How much is your monthly water bill? $")
            sewer = input("How much is you monthly sewer bill? $")
            gas = input("How much do you pay monthly for gas? $")
            otherUtilities = input("If you pay any other monthly fees for utilites, how much do you pay? $")
            pass
        else:
            electric = 0
            water = 0
            sewer = 0
            gas = 0
            otherUtilities = 0
            print("We'll take that as a no")
            pass
        hoaResponse = input("Do you pay HOA fees for the property? y/n ")
        if hoaResponse.lower() == 'n':
            hoa = 0
            pass
        elif hoaResponse.lower() == 'y':
            hoa = input("How much do you pay monthly for HOA fees? $")
            pass
        else:
            hoa = 0
            print("That's a no")
            pass
        print("\nWe recommend putting away money monthly for the following: ")
        print(r"5% of total monthly income for future vacancy expenses")
        print(r"5% of total monthly income for general repairs")
        print(r"5% of total monthly income for capital expenses (these are basically larger repairs)")
        print("\nWe will automatically calculate these expenses for you.")
        vacancy = self.income * .05
        repairs = self.income * .05
        capEx = self.income * .05
        propMgmt = self.income * .1
        try:
            totalMonthlyExpenses = float(mortgage) + float(tax) + float(insurance) + float(electric) + float(water) + float(sewer) + float(gas) + float(otherUtilities) + float(hoa) + float(lawn) + float(vacancy) + float(repairs) + float(capEx) + float(propMgmt)
        except ValueError:
            print("\nOne of your values was not entered as a number.")
            print("We will need to get your expenses again to get an accurate calculation")
            Calculator.userInputExpenses(self)
        print(f"\nYour total monthly expenses are ${totalMonthlyExpenses}")
        self.expenses = totalMonthlyExpenses
        Calculator.yearlyCashFlow(self)

    def yearlyCashFlow(self): 
            totalMonthlyCashFlow = self.income - self.expenses
            self.cashFlow = totalMonthlyCashFlow
            print("\nAs soon as we get your closing costs, we can calculate the ROI (Return on Investment) for your property.")
            Calculator.cashOnCash(self)
    
    
    def cashOnCash(self):   
        downPayment = input("\nWhat was your down payment on the property? $")
        closingCost = input("What were the closing costs on the house? $")
        rehabBudget = input("What is the cost of any repairs or updates you did when closing on the property? $")
        otherExpenses = input("If you had any other expenses, how much were they? $")
        try:
            totalInvestment = float(downPayment) + float(closingCost) + float(rehabBudget) + float(otherExpenses)
        except ValueError:
            print("\nOne of your values was not entered as a number.")
            print("We will need to get your closing costs again")
            Calculator.cashOnCash(self)
        cashRoi = ((self.cashFlow * 12) / totalInvestment) * 100
        print(f"Your total investment in the property at {self.address} was {totalInvestment}")
        print(f"Your yearly return on investment is {cashRoi}%. ")
        if cashRoi >=10:
            print("This is considered a great return on investment!")
        elif cashRoi > 7:
            print("This is considered a good return on investment.")
        elif cashRoi >=0:
            print("This property does not appear to have a good return on investment.")
        else:
            print("You're losing money buddy :( ")
        redo = input("If you have any other properties you would like to discuss, please input 'y' otherwise press enter: ")
        if redo == 'y':
            Calculator.userInputIncome(self)
        else:
            quit()


def runCalc():
    address1 = Calculator()
    address1.giveAverage()

runCalc()