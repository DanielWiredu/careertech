
no_of_item = int(input("Enter the number of items \n"))
expense_list = []
total_expense = 0
for x in range(no_of_item):
    #print(x)
    expense_list.append(int(input("Enter expense")))
    
total_expense = sum(expense_list)
print(total_expense)
#print(total_expense)

'''
laon amount
rate
payment made
noOfMonths
'''