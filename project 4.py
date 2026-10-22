to_do_list = []

while True:
    print("to do list:", to_do_list)
    add = input("What would you like to add if you are done adding type 'Done': ")
    print("Your to do list:", add)
    if add.lower() != 'done':
        to_do_list.append(add)
    elif add.lower() == 'done':
        print("Your to do list:", to_do_list)
        confirmation = input("are you sure you want to confirm this list ? 'Yes/No': ")
        if confirmation.lower() == 'no':
            decision = input("what is your decision ? add more or remove seomthing from the list ?")
            if decision.lower() == 'remove':
                remove = input("What would you like to remove from the list: ")
                if remove in to_do_list:
                    to_do_list.remove(remove)
                    print("Your to do list:", to_do_list)
                else:
                    print("Item not found in the list.")
            if decision.lower() == 'add':
                continue
        if confirmation.lower() == 'yes':
            print("Your final to do list:", to_do_list)
            break

with open("to_do_list.txt", "w") as file:
    for item in to_do_list:
        file.write(item + "\n")
        print("Your to do list has been saved to 'to_do_list.txt'.")
