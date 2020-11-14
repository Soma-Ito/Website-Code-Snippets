
import csv

# --- write csv --- #
# list method
with open('csv_example_list_method.csv', 'w', newline='') as f:
    header = ['x', 'y', 'z']
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerow(header)

    for x in range(101):
        y = 2 * x
        z = x * x
        csv_writer.writerow([x, y, z])

# dictionary method
with open('csv_example_dictionary_method.csv', 'w', newline='') as f:
    header = ['x', 'y', 'z']
    csv_writer = csv.DictWriter(f, fieldnames=header, delimiter='\t')
    csv_writer.writeheader()

    for x in range(101):
        y = 2 * x
        z = x * x
        csv_writer.writerow({'x': x, 'y': y, 'z': z})
