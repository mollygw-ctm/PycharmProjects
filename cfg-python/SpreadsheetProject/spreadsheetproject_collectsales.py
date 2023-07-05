import csv

def collect_sales():
    #
    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        sales = []
    # identify that the spreadsheet has a header - takes this into account
        has_header = True
    # this outputs month with sales
        for row in spreadsheet:
            # creates a variable which concatenates month and sales
            sales_collect = row['month'] + ' ' + row['sales']
            # prints result
            print(sales_collect)

# runs programme
collect_sales()