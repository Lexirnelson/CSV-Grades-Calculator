#Alexa Nelson
#This program takes in a csv file of students and their
#grades to calculate the average

import csv
student_dict = {}
found = False

print('Please enter the CSV file name with student grades:')
file = input('FILE> ')

print('Please enter the name of the student to calculate grades:')
student = input('STUDENT> ')

with open(file) as csv_file: #creates a dictionary from the the csv file
    reader = csv.reader(csv_file)
    for row in reader:
        student_dict[row[0]] = row
csv_file.close()

for x in student_dict:
    if x == student:#checks to see if the key name matches the student to look up
        found = True
        student_list = student_dict[x]#singles out the list of the student you want
        name = student_list[0]
        output = open('output.txt','w')
        output.write(name)
        output.write(', ')
        student_list.pop(0)#gets rid of the name so the list is just numbers
        total = 0
        maxim = 0
        minim = 100
        for x in student_list:#finds the max min and total
            total += int(x) 
            if int(x) > maxim:
                maxim = int(x)
            if int(x) < minim:
                minim = int(x)
        average = total / (len(student_list))#uses the total for the average
        output.write(str(int(average)))
        output.write(', ')
        output.write(str(maxim))
        output.write(', ')
        output.write(str(minim))
        output.close()
        print('The average grade for ', name, ' is: ', int(average))
        print('OUTPUT ', int(average))
        print('The maximum grade for ', name, ' is: ', maxim)
        print('OUTPUT ', maxim)
        print('The minimum grade for ', name, ' is: ', minim)
        print('OUTPUT ', minim)

if not found:
    print('Student not found. No output file created')
    print('OUTPUT error')
    
    























