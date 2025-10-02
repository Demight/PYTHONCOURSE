
expenses = [10, 20.5, 30, 40.6, 50]

def total_expenses(expenses):
    #return sum(expenses)  
    sum = 0
    for expense in expenses:
        sum = sum + expense
    return sum
  
print("Total expenses: $", total_expenses(expenses), sep = "")

