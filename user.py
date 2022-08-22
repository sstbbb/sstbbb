def login():

    database = {"admin": "password123"}
    username = ""
    password = ""

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in database:

        if database[username] == password:
            print("You did it!")
            print("Welcome back", username, "!")
        else:
            print("Wrong password")
            print("Please try again")
            password = input("Enter passord: ")
            print("Correct password")
            print("Welcome back", username, "!")
    else:
        print("User name not found. Please register.")


def register():

    database = {"admin": "password123"}
    username = ""
    password = ""

    if username in database:
        print("Username already registered.")
        return ""
    username = input("Enter username: ")
    password = input("Enter password: ")
    database[username] = password
    print("Username " + username, "registered!")
    return username
