# Determine the body-mass index of 6 individuals
# Include an array of 6 names
names = ["John", "Jane", "Bob", "Sally", "Arnold", "Sue"]
height = 0
weight = 0
heights = []
weights = []
bmi = []

# should call a function with height and weight as parameters that returns BMI ((weight x 703)/height^2)
def bmiCalc(height, weight):
  return ((weight * 703) / height**2)
  
# BMI as a parameter and returns if individual is underweight, normal weight or overweight
def bmiHealth(bmi):
  if bmi <= 20:
    return "underweight"

  elif bmi > 20 and bmi <= 30:
    return "normal weight"

  elif bmi > 30:
    return "overweight"

# Use a for loop to prompt user for height(in) and weight(lbs)

for i in names:
  # Include name of individual in each prompt
  height = int(input(f"{i}, enter your height in inches: "))
  heights.append(height)

  weight = int(input(f"{i}, enter you weight in lb: "))
  weights.append(weight)
  
  bmiResult = int(bmiCalc(height, weight))
  bmi.append(bmiResult)


  print(" ")

# Using a second loop it should traverse the array of BMI indices and call another function with BMI as a parameter and returns if individual is underweight, normal weight or overweight
j = 0
while j < 6:
  person = names[j]
  health = (bmiHealth(bmi[j]))
  print(f"{person} has a BMI of {bmi[j]} and is {health}.")

  j+=1
