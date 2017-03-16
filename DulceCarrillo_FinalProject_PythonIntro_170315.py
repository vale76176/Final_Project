#My final project is a function that can help me tackle my To Do List at work
#It will also help me differentiate between Projects

''''Include a function that takes at least two user arguments from the command line
Contain at least one if/else statement
Perform a calculation on a list
Use at least one dictionary
Have one try/except clause for every function
Output something (write) to a file, using string formatting
Must include docstrings telling us how to run your script.'''

# From a csv, create a dictionary of the number of defibrillators a customer ordered, csv will be on input argument #1.
# Report out how many total defibrillators are on order
# Report out how many customers have ordered more than a value to be entered when the program runs
# Write results to a file with filename on argument #2

import sys
import csv

def counting_function(workingdict):
    count = 0
    for key, value in workingdict.items():
        count = count + value
    return count

cmdargs = (sys.argv)
cmdlen = len(sys.argv)
workContacts_dict = dict(())
print(cmdargs)

with open(cmdargs[1])as f:
    reader = csv.reader(f)
    for row in reader:
        workContacts_dict[row[0]]=float(row[1])


print(workContacts_dict)

totalDefibrillators = counting_function(workContacts_dict)
print(totalDefibrillators)

minValue = input('Please enter the minimum order quantity to check against: ')
minValue = float(minValue)
CustomersOrderedMin = list()
DidNotOrderMin = list()

for key, value in workContacts_dict.items():
    if value >= minValue:
        CustomersOrderedMin.append(key)
        print('{} ordered the minimum quantity.'.format(key))
    else:
        DidNotOrderMin.append(key)
        print('{} did NOT order the minimum quantity.'.format(key))


print(CustomersOrderedMin)

f = open(cmdargs[2], 'w')
f.write('Total defibrillators ordered: {}\n'.format(totalDefibrillators))
if len(CustomersOrderedMin) > 0:
    f.write('Customers {} have ordered the minimum quantity of {} defibrillators.\n'.format(CustomersOrderedMin,minValue))
else:
    f.write('No customers ordered the minimum quantity of {} defibrillators.\n'.format(minValue ))

if len(DidNotOrderMin) > 0:
    f.write('Customers {} did not order the minimum quantity.\n'.format(DidNotOrderMin))
else:
    f.write('All customers ordered the minimum quantity.\n')

f.close()
