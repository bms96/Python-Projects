# Program to determine whether a password meets all the requirements for a secure password

while True:
  # Prompt the user for the candidate password
  password = input("What would you like your password to be? ")

  # Storing password length in variable
  passlength = len(password)

  # Variable to check for invalid sub strings
  passwordSubStringCheck = password.lower()


  # Password must be at least 6 characters
  if passlength < 6:
    print("Your password must be at least 6 characters long\n")
  
  # Password must be no longer than 12 characters
  elif passlength > 12:
    print("Your password must be less than 12 characters long\n")
  
  # Password cannot contain 'umgc' in any combination of lower or upper case letters
  elif "umgc" in passwordSubStringCheck:
    print("The password cannot contain 'umgc' in any case\n")

  # Checking to see if the first or last character in password contains '#'
  elif password[0] == "#" or password[-1] == "#":
    print("Cannot have '#' as first or last character in password\n")
  
  # Checking that the password contains '#'
  elif "#" not in password:
    print("Password must contain '#'\n")

  else:
    print("You have entered a valid password")
    break
