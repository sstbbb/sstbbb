from donations_pkg import homepage, user

database = {"admin": "password123"}
donations = []
authorized_user = ""


homepage.show_homepage()

if len(authorized_user) == 0:
    print("You must be logged in to donate.")
else:
    print("Logged in as:", authorized_user)


while True:

    option = input("Choose an option: ")


    if option == "1":
        user.login()
    elif option == "2":
        user.register()
    elif option == "3":
        homepage.donate()
    elif option == "4":
        print("TODO: Write Donations Functionality.")
    else:
        option == "5"
        print("See You later!")
        break
