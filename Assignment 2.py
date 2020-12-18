
    # Discounted price for children
    if age >= 0 and age <= 12:
      ageCategory = "child"
      ticketPrice = 10
      print("")
      break

    elif age > 12 and age < 65:
      ageCategory = "adult"
      ticketPrice = 14
      print("")
      break

    # Discounted price for seniors
    elif age >= 65:
      ageCategory = "senior"
      ticketPrice = 12
      print("")
      break

    else:
      print("\nPlease enter a vlaue greater than or equal to 0. ")

  except ValueError:
      print("\nYou entered an invalid answer. Please only enter numbers.")

while True:
  try:
    # Asking if customer would like to see movie in 3D
    is3D = input("Would you like to see the movie in 3D for only 3 more dollars? Type 'yes' or 'no' ")
    is3D = is3D.upper()

    # 3D ticket will be $3 more
    if is3D == "YES":
      ticketPrice += 3
      print("")
      # Output of final ticket value of 3D ticket
      print(f"The total cost the {ageCategory} ticket in 3D is ${ticketPrice}")
      break

    # No adjustment to ticket price if no
    elif is3D == "NO":
      # Output of final ticket value of non-3D ticket
      print(f"The total cost your {ageCategory} ticket is ${ticketPrice}")
      print("")

      break

    else:
      print("\nPlease enter either 'yes' or 'no'.")
    # except ValueError:
  except :
    print("\nplease enter yes or no")

# Output of final ticket value
