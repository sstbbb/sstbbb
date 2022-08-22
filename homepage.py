def show_homepage():

    print("         === DonateMe Homepage ===           ")
    print("-------------------------------------------  ")
    print("| 1.   Login        | 2.   Register         |")
    print("-------------------------------------------  ")
    print("| 3.   Donate       | 4.   Show Donations   |")
    print("-------------------------------------------  ")
    print("|                5. Exit                    |")
    print("-------------------------------------------  ")


def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_amt = float(donation_amt)
    print(username, "donated", donation_amt)
    print("Thank you so much")
