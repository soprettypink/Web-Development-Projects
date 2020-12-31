#Create a function that finds the average of the grades
def Average(grades):
    return sum(grades) / len(grades)

#Creates an empty list
grades = []

#Prompts the user to enter the number of grades
#Prompts the user to enter each grade before printing them out in the form of a list
num = int(input("Enter the number of grades: "))
for i in range(0, num):
    print("Please enter a grade: ")
    item = int(input())
    grades.append(item)
    
print("The grades entered are: ", grades)

#Asks the user if the program should continue or end prematurely
while True:
    if input("Continue? ") != 'y':
        break
    break

print(" ")

average = Average(grades)
print("The average is ", round(average, 2))
print(" ")

#Prompts the user to add in 5 more grades into the list
print("There are 5 more grades that must be entered into the list.")
for i in range(5):
    print("Please add in another grade: ")
    item = int(input())
    grades.append(item)
    
print("The grades that have been entered are: ", grades)
while True:
    if input("Continue? ") != 'y':
        break
    break

print(" ")
    
#Modifies several grades in the list
for i in range(2):
    print("Which grade on the list would you like to update?")
    item = int(input())
    print("Please enter the updated grade.")
    grades[item] = int(input())

print("The updated grades are: ", grades)
while True:
    if input("Continue? ") != 'y':
        break
    break

print(" ")

#Prompts the user to enter in 2 more grades into the list
print("Please add in 3 more grades into the list.")
for i in range(3):
    print("Enter a grade: ")
    item = int(input())
    grades.append(item)

#Modifies the last three grades and prints out the entire list
print("Please enter 3 new grades to make the final updates for the grades.")
digit = 9
while digit <= 11:
    grades[digit] = int(input())
    digit += 1
print("The final updates for the grades are complete.")
print("The grades are ", grades)
print(" ")

#Sorts the grades in the list from smallest to largest
sorted_grades = sorted(grades)
print("The grades listed in numerical order are ", sorted_grades)
while True:
    if input("Continue? ") != 'y':
        break
    break

print(" ")

#Finds the average of the grades
average = Average(grades)
print("The average is ", round(average, 2))

#Displays the final grade for the entire course
if average <= 100 and average >= 90:
    print("You have received an A in the course! Congratulations!")
elif average <= 89 and average >= 80:
    print("You have received a B in the course! Good Job!")
elif average <= 79 and average >= 70:
    print("You have received a C in the course. Nice try!")
elif average <= 69 and average >= 60:
    print("You have received a D in the course. Please try harder next time.")
else:
    print("You have failed the course. You must retake the course.")
    
