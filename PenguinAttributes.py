#importing the python libraries I will need
import matplotlib.pyplot as plt
import csv
from time import sleep
from numpy import array, average
global idnum
#creating empty lists
flen = []
billl = []
billd = []
bmass = []
idno = []
# opnening the file and filling my empty lists with data from the csv file
with open('clean_penguins.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for col in data:
        bmass.append(col['body_mass_g/100'])
        flen.append(col["flipper_length_mm"])
        billl.append(col["bill_length_mm"])
        billd.append(col['bill_depth_mm'])
        idno.append(int(col['id']))
        mass = [float(x) for x in bmass]
        flip = [float(x) for x in flen]
        bill = [float(x) for x in billl]
        depth = [float(x) for x in billd]
# for the bar plot
def barplot(data):
    idnum = int(input("Please enter penguin ID number"))
    if idnum > 333:
        print("please enter a valid value")
        barplot(data)
    elif idnum < 1:
        print("please enter a valid value")
        barplot(data)
    q = str(idno[idnum-1])
    a = bill[idnum-1]
    b = depth[idnum-1]
    c = flip[idnum-1]
    d = mass[idnum-1]
    Attribute = ['bill_length', 'bill_depth', 'flipper', 'mass']
    Value = [a, b, c, d]
    plt.bar(Attribute, Value, width=1)
    plt.title("Measurement for sample " + q)
    plt.xlabel("Atrribute")
    plt.ylabel("Value")
    plt.show()
    init_function()
# function for the scatter plot
def scatter(data):
    print("Please choose an attribute to compare against the other attributes\n the
attributes are as follows:\n bill_length_mm\n bill_depth_mm\n flipper_length_mm\n
body_mass_g/100\n")
    scatterchoice = input("Please enter attribute?")
    if scatterchoice == "bill_length_mm":
        x = bill
        w = [[mass],
            [flip],
[depth] ]
        avg = array(w)
        column_average = average(avg, axis=0)
        y = column_average
    elif scatterchoice == "bill_depth_mm":
        x = depth
        w = [[mass],
            [flip],
[bill] ]
        avg = array(w)
        column_average = average(avg, axis=0)
        y = column_average
    elif scatterchoice == "flipper_length_mm":
        x = flip
        w = [[mass],
            [bill],
[depth] ]
        avg = array(w)
        column_average = average(avg, axis=0)
        y = column_average
    elif scatterchoice =="body_mass_g/100":
        x = mass
        w = [[bill],
            [flip],
            [depth]
        ]
        avg = array(w)
        column_average = average(avg, axis=0)
        y = column_average
    else:
        print('Invalid input please choose enter the corect option')
        scatter(data)
    plt.title(scatterchoice + " comparison")
    plt.xlabel("Body_mass_g/100 measurement")
    plt.ylabel("Average of other attributes")
    plt.xlim(0,250)
    plt.ylim(0,150)
    plt.scatter(x,y)
    plt.plot([0,250],[0,150])
    plt.show()
    init_function()
# a function for the main program
sleep = 2
def init_function():
    print("Welcome to penguin attribute analysis")
    print("Please choose one of the following\n 1 - display a bar plot of penguin's
measuremeants\n 2 - display a scatter plot of attribute's measurements\n 3 - exit
the system\n")

choice = input("Your choice?")
    if choice == "1":
        barplot(data)
    elif choice == "2":
        scatter(data)
    elif choice == "3":
        print("please press Enter to exit program")
        exit()
    else:
        print("Invalid input please choose the correct option")
        init_function()
init_function()
