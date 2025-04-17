
from urllib.request import urlopen

def readFileURLString(url):
    data = urlopen(url)
    html_data = data.read()
    encoding = data.headers.get_content_charset('utf-8')
    decoded_html = html_data.decode(encoding)
    return decoded_html


data_str = readFileURLString("https://www.gutenberg.org/cache/epub/11/pg11.txt")
print(data_str)
# Question 1
'''

pick 5 books
read 4 of 5 books
write each of the 4 books into a separate fi;le aitomate this processs as much as possibe.
thw 5th book tot;es keep in mind but dont read/write it
use try-except block to do the following
read number of words of the story only
find frequence of each word in file 
no of paragrpahs
no of sentences
length of smallest and longest word, averge length
modt common vowel
what is the average isage of punction makrks for every 100 sentences \



QUestion 2
Open your story file from class for reading.
(a) Print the story (only the story) for the user to read
(b) Count the total number of words in the story
(c) Count the frequency of each word in the story.  Then sort all the available words
    in the story according to their frequence from highest to lowest. Display the results.
'''

# # Question 2
# '''
# Make two files: cats.txt and dogs.txt.  Store at least three names of cats in the first
# file and three names of dogs in the second file.  Write a program that tries to read
# these files and print the contents of each file to the screen.  

# (a) Wrap your code in a try-except block to catch the FileNotFoundError and print a 
#     friendly message if a file is missing.  To test your code, move one of the files 
#     to a different location on your system, and make sure that the code in the except 
#     block executes properly.  
# (b) Modify your previous code to fail silently if either file is missing
# '''

# # Question 3
# '''
# A common problem when prompting for numerical input occurs when providing text 
# instead of numbers.  In such a case, when trying to convert the input to int, a
# ValueError occurs.  Write a program that prompts the user for two numbers, add
# them together and print the result.  Catch the ValueError if either input value is
# not a number, and print a friendly error message.  Test your program by entering two
# numbers and then by entering some text instead of a number.  
# '''

# Question 4
# '''
# Using the json module write student information to the file in JSON format.  
# That is, create a dictionary of of student data in the following format: 
# gradebook_dict = {'students': [student1dictionary, student2dictionary, ...]}. 

# Each dictionary in the list represents one student and contains the keys:
# 'first_name', 'last_name', 'exam1', 'exam2' and 'exam3'.  The keys map to the
# values represengint each student's first name (string), last name (string) and 
# three exam scores (integers).  

# Output the gradebook_dict in JSON format to the file grades.json.  
# '''

# Question 5
# '''
# Using the json module to read the grades.json file created in the previous
# question.  Display the data in tabular format, including an additional 
# column showing each student's average to the right of the student's three
# exam grades and an additional row showing the class average on each exam.  
# '''


#Question 2

file_txt = open("cats.txt", 'w')

file_txt.write("James\nOk\nCOol\n")

file2_txt = open("dogs.txt", 'w')

file2_txt.write("James\nOk\nCOol\n")


try:
    file_txt = open("cats.txt", "r")
    print("Contents of cats.txt:")
    print(file_txt.read())  
    
    file2_txt = open("dogs.txt", "r")
    print("Contents of dogs.txt:")
    print(file2_txt.read())  

except FileNotFoundError:
    print(f"Error")
    #OR
    pass

#Question 3
# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1+num2)
# except ValueError:
#     print("OOPS")

# Question 4

import json

gradebook = {
    "students": [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "exam1": 85,
            "exam2": 90,
            "exam3": 88
        },
        {
            "first_name": "Bob",
            "last_name": "Johnson",
            "exam1": 78,
            "exam2": 82,
            "exam3": 80
        },
        {
            "first_name": "Charlie",
            "last_name": "Brown",
            "exam1": 92,
            "exam2": 87,
            "exam3": 91
        }
    ]
}

with open('grades.json', 'w') as file:
    json.dump(gradebook, file)

import json

with open('grades.json', 'r') as file:
    gradebook = json.load(file)

students = gradebook['students']

print(f"{'First Name':<12} {'Last Name':<12} {'Exam 1':<8} {'Exam 2':<8} {'Exam 3':<8} {'Average':<8}")
print("-" * 56)

for student in students:
    avg = (student['exam1'] + student['exam2'] + student['exam3']) / 3
    print(f"{student['first_name']:<12} {student['last_name']:<12} {student['exam1']:<8} {student['exam2']:<8} {student['exam3']:<8} {avg:<8.2f}")

class_avg1 = sum(student['exam1'] for student in students) / len(students)
class_avg2 = sum(student['exam2'] for student in students) / len(students)
class_avg3 = sum(student['exam3'] for student in students) / len(students)

print("-" * 56)

print(f"{'Class Avg':<24} {class_avg1:<8.2f} {class_avg2:<8.2f} {class_avg3:<8.2f}")