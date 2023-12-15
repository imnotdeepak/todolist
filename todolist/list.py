import argparse

FILENAME = "todo.txt" # creates file to store actions in the list

def add_strikethrough(item): 
    return f"\x1b[9m{item}\x1b[0m" # bash code to cross out stuff

def add_item(item): # this function adds items to the to do list
    with open(FILENAME, "a") as file:
        file.write(f"{item}\n")
        file.close()
    print(f"Added item: {item}")

def list_items(): # this function lists every action that the user has stored
    lines = None
    try:
        with open (FILENAME, "r") as file: # opens the file to read
            lines = file.readlines()
    except FileNotFoundError: # in case the file cannot be detected
        print(f"Error: File '{FILENAME}' not found.")

    if not lines: # if there are no items stored in the file
        print("no items found.")
    else:
        for i, line in enumerate(lines):
            print(f"{i+1}. {line.strip()}")

def mark_item_done(item_number): # this function crosses out any items that have been completed
    with open(FILENAME, "r") as file:
        lines = file.readlines()

    if not lines: # this makes sure that the number corresponding to the item is correct
        print("No items found.")
    elif item_number < 1 or item_number > len(lines):
        print("Invalid item number")
    else:
        item = lines[item_number-1].rstrip()
        item = add_strikethrough(item)
        with open(FILENAME, "w") as file:
            for i, line in enumerate(lines):
                if i == item_number-1:
                    file.write(f"{item}\n")
                    print(f"Marked item as complete: {item}")
                else:
                    print(line)
                    file.write(line)

if __name__ == "__main__": # these are the actions of the functions above
    parser = argparse.ArgumentParser(description="Manage your to-do list")
    parser.add_argument("action", choices=["add", "list", "done"], help = "action to perform")
    parser.add_argument("--item-text", help = "Text of the item to add")
    parser.add_argument("--item-number", type = int, help = "Number of the item to mark done")
    args = parser.parse_args()

    if args.action == "add":
        add_item(args.item_text)
    elif args.action == "done":
        mark_item_done(args.item_number)
    elif args.action == "list":
        list_items()
