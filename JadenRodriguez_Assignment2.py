# Program Name: JadenRodriguez_Assignment2.py
# Course: IT3883/Section W01
# Student Name: Jaden Rodriguez
# Assignment Number: 2
# Due Date: 10/02/2026
# Purpose: This program reads student names and six test scores from a text file,
#          calculates each student's average, and prints the results in descending order by grade.
# Specific resources used to complete the assignment: None

#Create an empty list to store the students and their calculated averages
student_list = []

#Opens the input txt file
file = open("Assignment2input.txt", "r")

#Loops through each line in the file one by one
for line in file:
    #Splits the line into a list of strings based on spaces
    data = line.split()

    #Lists the student's name as first data point
    name = data[0]

    #Converts the 6 scores from text to numbers 
    score1 = float(data[1])
    score2 = float(data[2])
    score3 = float(data[3])
    score4 = float(data[4])
    score5 = float(data[5])
    score6 = float(data[6])

    #Calculates the total of all scores and divides by 6 for the average
    total_score = score1 + score2 + score3 + score4 + score5 + score6
    average = total_score / 6

    #Adds the average and name to list as small list
    #Puts average first so that it can be used to sort the data later
    student_list.append([average, name])

#Closes the input file to free up system resources
file.close()

#Sorts the list of students
#reverse=True makes it sort from highest  to lowest
student_list.sort(reverse=True)

#Loops through the sorted list to print out final results
for student in student_list:
    #Retrieves average and name from the list
    student_average = student[0]
    student_name = student[1]

    #Prints the name and the average formatted to exactly 2 decimal places
    print(f"{student_name} {student_average:.2f}")