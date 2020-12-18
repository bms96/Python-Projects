# compute the average and highest quiz grade for a group of five students

# For computing the average grade
import statistics

# List of five names
students = ["Bryan", "Jen", "Mike", "Matt", "Dena",]

# List for grades to be stored in and analyzed
grades = []

# Using a for loop, it should successively prompt the user for the quiz grade for each of the five students
for i in students:
  grade = int(input(f"{i}, what grade did you get on your quiz? "))

  # Storing entered data and appending that data to the grades list
  grades.append(grade)
  
# Taking the average of the grades  
average_grade = statistics.mean(grades)

# Taking the highest grade  
highest_grade = max(grades)

# Printing out the results of highest grade and average of all the grades entered
print("\n")
print(f"The highest grade is {highest_grade}%")
print(f"The average grade is {average_grade}%")
