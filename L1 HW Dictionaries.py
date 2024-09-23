# Dictionary containing ten usernames and passwords
users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
    "user6": "password6",
    "user7": "password7",
    "user8": "password8",
    "user9": "password9",
    "user10": "password10"
}

# Prompt the user to enter their username and password
username = input("Enter your username: ")


# Check if the username is in the dictionary
if username in users:
    password = input("Enter your password: ")
    # Check if the password is correct
    if users[username] == password:
        print("You are now logged in to the system.")
    else:
        print("Invalid password.")
else:
    print("You are not a valid user of the system.")