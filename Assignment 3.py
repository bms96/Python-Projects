# This program calculates the cost of carpeting a room

# Prompt for the height and width of the room and store into a variable
width_of_room = int(input("Width of the carpeted area: "))
height_of_room = int(input("Height of carpeted area: "))

# Ask for the desired quality of the carpet
quality_of_carpet = input("Enter one of the following numbers for the quality of carpet to be used:\n'3' - High Quality ($10/sqft)\n'2' - Medium Quality ($8sq/ft)\n'1' - Low Quality ($5/sqft)\n")

# A function that takes in the height, width and quality of carpet
def carpet_cost(width_of_room, height_of_room, quality_of_carpet):
  total_sqft = width_of_room * height_of_room 
  total_price = 0
  
  # Highest quality of carpet chosen calculation and output total
  if quality_of_carpet == "3":
    total_price = total_sqft * 10
    print(f"The total cost of the carpet is ${total_price}")
    # Medium quality and output total
  elif quality_of_carpet == "2":
    total_price = total_sqft * 8
    print(f"The total cost of the carpet is ${total_price}")
    # Lowest quality and output total
  elif quality_of_carpet == "1":
    total_price = total_sqft * 5
    print(f"The total cost of the carpet is ${total_price}")
  else:
    print("Something went wrong")
    
# calling the function and passing through the required parameters
carpet_cost(width_of_room, height_of_room, quality_of_carpet)
