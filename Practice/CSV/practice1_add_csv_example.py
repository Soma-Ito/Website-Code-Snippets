
import csv

# --- add data --- #
# list method
with open('csv_example_list_method.csv', 'a', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',')

    for x in range(101, 201):
        y = 2 * x
        z = x * x
        csv_writer.writerow([x, y, z])

# dictionary method
with open('csv_example_dictionary_method.csv', 'a', newline='') as f:
    header = ['x', 'y', 'z']
    csv_writer = csv.DictWriter(f, fieldnames=header, delimiter='\t')

    for x in range(101, 201):
        y = 2 * x
        z = x * x
        csv_writer.writerow({'x': x, 'y': y, 'z': z})
