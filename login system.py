import os
import hashlib

FILE = "users.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    users = {}
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    users[parts[0]] = parts[1]
    return users

def save_user(username, hashed_password):
    with open(FILE, "a") as f:
        f.write(f"{username},{hashed_password}\n")

def register(users):
    print("\n--- Register ---")
    username = input("Choose a username: ").strip()
    if username in users:
        print(" Username already exists! Try a different one.")
        return
    password = input("Choose a password: ").strip()
    if len(password) < 6:
        print(" Password must be at least 6 characters!")
        return
    confirm = input("Confirm password: ").strip()
    if password != confirm:
        print(" Passwords do not match!")
        return
    hashed = hash_password(password)
    users[username] = hashed
    save_user(username, hashed)
    print(f" Account created successfully! Welcome, {username}!")

def login(users):
    print("\n--- Login ---")
    username = input("Enter username: ").strip()
    if username not in users:
        print(" Username not found!")
        return False, None
    password = input("Enter password: ").strip()
    if hash_password(password) == users[username]:
        print(f" Login successful! Welcome back, {username}!")
        return True, username
    else:
        print(" Incorrect password!")
        return False, None

def dashboard(username):
    print(f"\n Dashboard — Logged in as: {username}")
    print("You can add more features here!")
    input("Press Enter to logout...")

def main():
    print("=== Login System ===")
    users = load_users()
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            register(users)
        elif choice == "2":
            success, username = login(users)
            if success:
                dashboard(username)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
