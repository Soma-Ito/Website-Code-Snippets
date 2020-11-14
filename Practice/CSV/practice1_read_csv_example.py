
import csv

# --- read csv --- #
# list method
with open('csv_example_list_method.csv', 'r') as g:
    csv_reader = csv.reader(g, delimiter=',')

    next(csv_reader)
    for row in csv_reader:
        print(row)

# dictionary method
with open('csv_example_dictionary_method.csv', 'r') as g:
    csv_reader = csv.DictReader(g, delimiter='\t')

    for row in csv_reader:
        print(row)

import csv

# --- read csv --- #
# list method
with open('csv_example_list_method.csv', 'r') as g:
    csv_reader = csv.reader(g, delimiter=',')

    next(csv_reader)
    for row in csv_reader:
        print(row)

# dictionary method
with open('csv_example_dictionary_method.csv', 'r') as g:
    csv_reader = csv.DictReader(g, delimiter='\t')

    next(csv_reader)
    for row in csv_reader:
        print(row)
