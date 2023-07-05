from csv import writer

year = input('What year would you like to enter?')
month = input('What month would you like to enter?')
sales = input(('What were the sales for {}?').format(month))
expenditure = input(('What was the expenditure for {}?').format(month))

list = [year, month, sales, expenditure]

with open('sales.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(list)

    f_object.close()

