import json
from getpass import getpass
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Load users from file or start empty
try:
    with open("users.json", "r") as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}

print("=== Login System ===")

while True:  # continuous menu
    print("\n1. Login")
    print("2. Register")
    choice = input("Select an option (1 or 2, or 'q' to quit): ")

    if choice.lower() == 'q':
        print("Exiting program.")
        break

    # --- Registration ---
    elif choice == "2":
        new_username = input("Choose a username: ")
        if new_username in users:
            print("Username already exists. Please choose another one.")
        else:
            new_password = getpass("Choose a password: ")
            users[new_username] = hash_password(new_password)

            # Save to file
            with open("users.json", "w") as f:
                json.dump(users, f)

            print(f"User '{new_username}' registered successfully! You can now log in.")

    # --- Login ---
    elif choice == "1":
        attempts = 3
        while attempts > 0:
            username = input("Enter username: ")
            password = getpass("Enter password: ")

            if username in users and hash_password(password) == users[username]:
                print(f"Login successful! Welcome, {username}!")
                break
            else:
                attempts -= 1
                print("Incorrect credentials. Attempts left:", attempts)

        if attempts == 0:
            print("Account locked. Too many failed attempts.")

    else:
        print("Invalid option. Please select 1, 2, or 'q'.")

