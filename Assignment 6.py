# Read in temps for 10 days in C and store into array
while i > 0:
  # Try/Except to catch anything other than number from being entered
  try:
    day_temp = int(input(f"Enter the temperature of day {days_in} in C: "))

    # Appending input into temps array
    temps.append(day_temp)

    days_in += 1
    i -= 1

    # Create a new line after last prompt is entered
    if i == 0:
      print("\n")
      
  except ValueError:
    print("\nYou can only enter numbers.")

# Loop over and print out converted temps and count the type of day
for i in temps:
  # Convert each element in array to F
  # F = (C x 1.8) + 32
  f = round(((i *1.8) + 32), 1)
  print(f"The temperature for day {days_out} is {f}F")

  # Determing thresholds and accounting for the number of cool, warm and hot days

  # Cool days
  if f <= 70:
    print("It was a cool day\n")
    cool += 1

  # Warm Days
  elif f > 70 and f < 85:
    print("It was a warm day\n")
    warm += 1

  # Hot Days  
  elif f >= 85:
    print("It was a hot day\n")
    hot +=1

  days_out += 1
  i += 1

# Count number of cool, warm, and hot days
print(f"Number of cool days: {cool}\nNumber of warm days: {warm}\nNumber of hot days: {hot}\n")

# Display entire array
print(f"Elements of user input (Celsius) \n{temps}")
