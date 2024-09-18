expenses = []
num_expenses = int(input("Enter # of expenses:"))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expenses:")))

total = sum(expenses)
print("You spent $", total, sep='')