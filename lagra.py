users = {
    "Erik":"12345",
    "Oliver":"54321",
    "Chengzi":"Huang"
}

items = {
    "Erik":["vante", "mössa"],
    "Oliver":["skor", "cykel"],
    "Chengzi":["dator", "boll", "bil"]
}

def check_login(username, password):
    if(username in users and password == users[username]):
        return True
    return False

def list_items(username):
    print("\nThese are your items\n")

    for num, item in enumerate(items[username]):
        print(f"{num+1}) {item}")

def add_item(username):
    item = input("\nAdd item: ")
    items[username].append(item)

def login():
    username = input("\nUser: ")
    password = input("Password: ")

    if(check_login(username, password)):
        print(f"\nWelcome {username}")
        return username
    return False

def actions(username):
    print("\nSelect an action\n")
    print("a) Add item")
    print("l) List items")
    print("q) Log out\n")

    action = input("Option: ")

    match action:
        case "a":
            add_item(username)
            actions(username)
        case "l":
            list_items(username)
            actions(username)
        case "q":
            print()
            opt()
        case _:
            print("\nInvalid input, try again")
            actions(username)


def opt(tryagain=False):
    if tryagain:
        print("\nr) Try again")
    else:
        print("l) Log in")
    print("q) Quit\n")
    option = input("Option: ")

    if(option == "l" and tryagain == False) or (option == "r" and tryagain == True):
        username = login()
        if(not username):
            opt(True)
        else:
            actions(username) 
    elif(option == "q"):
        quit()
    else:
        if tryagain:
            print("\nInvalid input, try again")
        else:
            print("\nInvalid input, try again\n")
        opt(tryagain)



if __name__ == "__main__":
    print("Welcome to Lagra (TM)\n")
    opt()