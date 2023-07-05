import csv

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    sales = []

    for row in spreadsheet:
        pizza_sales = row['sales']
        sales.append(pizza_sales)

def highest_sale():
    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)

        sales = []
        for row in spreadsheet:
            bamboo_sales = row['sales'] + " in " + row['month'] + " " + row['year']
            sales.append(bamboo_sales)

    highest_sale_month = max(sales)
    print(('The highest sale was £{}').format(highest_sale_month))

highest_sale()

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

lowest_sale()

# how to obtain the key within a dictionary
def dictionary():
    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        sales = []
    print(sales)
dictionary()