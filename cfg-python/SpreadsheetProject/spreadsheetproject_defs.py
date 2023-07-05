import csv
import pandas as pd
#import numpy as np
from csv import writer

# reads csv file
df = pd.read_csv('sales.csv')


# Adding entry to sales.csv
# option a
def add_entry():
    year = input('Which year would you like to enter?')
    month = input('Which month would you like to enter?')
    sales = input(('What were the sales for {} {}?').format(month, year))
    expenditure = input('What was the expenditure for {} {}?'.format(month, year))

    list = [year, month, sales, expenditure]

    with open('sales.csv', 'a') as csv_file:
        writer_object = writer(csv_file)
        writer_object.writerow(list)

        csv_file.close()

    print("This has been added to the CSV file.")

# Finding highest sales
# option b
def highest_sale():
    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)

        sales = []
        for row in spreadsheet:
            bamboo_sales = row['sales'] + " in " + row['month'] + " " + row['year']
            sales.append(bamboo_sales)

    highest_sale_month = max(sales)
    print(('The highest sale was £{}').format(highest_sale_month))

# Finding lowest sale
# option c
def lowest_sale():
    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)

        sales = []
        for row in spreadsheet:
            bamboo_sales = row['sales'] + " in " + row['month'] + " " + row['year']
            sales.append(bamboo_sales)

    lowest_sale_month = min(sales)
    print(('The lowest sale was £{}').format(lowest_sale_month))

# Calculates average
# option d
def average():
    # converts column of sales to a list
    sales_list = df['sales'].tolist()
    # finds sum of the sales list
    total = (sum(sales_list))
    # finds number of entries
    number_of = (len(sales_list))
    # prints mean value to 2 decimal places
    mean = round((total / number_of),2)
    print("The average sales are £{}".format(mean))

# Calculates total
# option e
def total_sales():
    # converts column of sales to a list
    sales_list = df['sales'].tolist()
    # finds sum of the list
    total = (sum(sales_list))
    print("The sales total is £{}".format(total))

# Prints out sales for each month
# option f
def collect_month_sales():
    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        sales = []
        has_header = True
        for row in spreadsheet:
            sales_collect = row['month'] + ' £' + row['sales']
            print(sales_collect)


def sales_only_column():
    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        sales = []

        has_header = True

# this outputs month with sales
        for row in spreadsheet:
            sales_collect = row['sales']
            print(sales_collect)

# converts sales column into a list
def sales_column_as_list():
    # converting column data to list
    sales = df['sales'].tolist()

    print(sales)

# calculates number of entries
def number_of_entries():
    # converting column data to list
    sales_list = df['sales'].tolist()
    # find number of entries in list
    print(len(sales_list))


print("What would you like to do? Here are your options:")
print("a) add an entry")
print("b) find highest sale")
print("c) find lowest sale")
print("d) calculate average of sales")
print("e) calculate total sum of sales")
print("f) print sales from each month")
answer = input("Please enter a letter")

if answer == 'a':
    add_entry()
elif answer == 'b':
    highest_sale()
elif answer == 'c':
    lowest_sale()
elif answer == 'd':
    average()
elif answer == 'e':
    total_sales()
elif answer == 'f':
    collect_month_sales()
else:
    print("try again")

