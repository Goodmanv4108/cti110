#CTI-110
#P4HW1 - Expenses
#Veronica Goodman
#3/31/2020




#The expenses variable.
expenses = 0
#The number of expenses variable.
NumberExpenses = 1
#The number of expenses variable.
expansion = 'Y'
#Getting the amount in the bank acount.
BankAmount = float(input('Enter the Starting amount in Your account: '))

#Choosing if they want to add another expense or not.
while expansion == 'Y' or expansion == 'y':
#Getting the expense amount(s)
    expense=float(input('Enter expense amount {}: '. format(NumberExpenses)))
#The number of amounts entered.
    NumberExpenses += 1
#Getting input if they want to add another.
    expansion = input('Do you want to enter another expense? (Y/N)')
    expenses += expense
#Getting the final amount.
    amount = BankAmount - expenses
    NumberExpenses = NumberExpenses - 1

#Printing out the final answers of how much was in the bank before, how many expenses were inputed and the amount after the expenses were subtracted.

print('Amount in bank account before expenses subtracted: ${:,.2f}'.format(BankAmount))


print('Number of expenses entered:',NumberExpenses)


print('Amount in account after expenses subtracted: ${:,.2f}'.format(amount))
