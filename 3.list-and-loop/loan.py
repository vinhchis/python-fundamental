# get detail of loan
money_owed = float(input('How much money do you owe, in dollars ?\n')) # $20,000
apr = float(input('What is annual percentage rate of the loan ?\n')) # 3%
payment = float(input('How much will you pay off each month in dollars?\n')) # $1,000
months = int(input("How many months do you want to see the results for ?\n")) # 24


monthly_rate = apr/100/12

for month in range(1, months):
    # Calculate interest to pay
    interest_paid = monthly_rate * money_owed

    # Add in interest
    money_owed = money_owed + interest_paid


    if(money_owed - payment <= 0):
        print("After", str(month), ',you already paid off the loan')
        print("The last payment is", money_owed)
        break

    # Make payment
    money_owed = money_owed - payment

    print('In', str(month),'Paid', payment , 'of which',interest_paid ,'was interest.', end=' ')
    print('Now I owe', money_owed)

