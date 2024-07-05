import time
from datetime import datetime

class User:
    def __init__(self, user_id, name, address, phone_number, email):
        self.user_id = user_id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def display_user(self):
        print(f"User ID: {self.user_id}\nName: {self.name}\nAddress: {self.address}")
        print(f"Phone Number: {self.phone_number}\nEmail: {self.email}")

class Computer:
    def __init__(self, computer_id, memory_capacity, processor_model, motherboard_company):
        self.computer_id = computer_id
        self.memory_capacity = memory_capacity
        self.processor_model = processor_model
        self.motherboard_company = motherboard_company

    def display_computer(self):
        print(f"Computer ID: {self.computer_id}\nMemory Capacity: {self.memory_capacity}")
        print(f"Processor Model: {self.processor_model}\nMotherboard Company: {self.motherboard_company}")

class CafeManagementSystem:
    def __init__(self):
        self.users = []
        self.computers = []
        self.login_times = {}

    def login(self):
        password = input("Enter password: ")
        if password == "admin":
            print("Login successful!")
        else:
            print("Incorrect password!")

    def add_user(self):
        user_id = input("Enter User ID: ")
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        self.users.append(User(user_id, name, address, phone_number, email))
        print("User added successfully!")

    def display_users(self):
        for user in self.users:
            user.display_user()
            print("-----------------------")

    def add_computer(self):
        computer_id = input("Enter Computer ID: ")
        memory_capacity = input("Enter Memory Capacity: ")
        processor_model = input("Enter Processor Model: ")
        motherboard_company = input("Enter Motherboard Company: ")
        self.computers.append(Computer(computer_id, memory_capacity, processor_model, motherboard_company))
        print("Computer added successfully!")

    def display_computers(self):
        for computer in self.computers:
            computer.display_computer()
            print("-----------------------")

    def book_computer(self, user_id, computer_id):
        now = time.time()
        self.login_times[user_id] = now
        print(f"Computer booked successfully for user {user_id}")

    def logout_computer(self, user_id):
        now = time.time()
        if user_id in self.login_times:
            start_time = self.login_times[user_id]
            duration = (now - start_time) / 60  # duration in minutes
            print(f"User {user_id} logged out. Duration: {duration:.2f} minutes.")
            del self.login_times[user_id]
        else:
            print("User not logged in.")

    def calculate_charges(self, user_id):
        now = time.time()
        if user_id in self.login_times:
            start_time = self.login_times[user_id]
            duration = (now - start_time) / 60  # duration in minutes
            charges = duration * 0.5  # assume $0.5 per minute
            print(f"Charges for user {user_id}: ${charges:.2f}")
        else:
            print("User not logged in.")

    def renew_membership(self, user_id):
        print(f"Membership for user {user_id} renewed successfully.")

    def save_data(self):
        # Placeholder for save logic
        print("Data saved successfully.")

    def load_data(self):
        # Placeholder for load logic
        print("Data loaded successfully.")

def main():
    system = CafeManagementSystem()
    system.load_data()
    system.login()

    while True:
        print("1. Master Entry\n2. Cafe Management\n3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            while True:
                print("1. Add New Member\n2. Show Member\n3. Update Record\n4. Delete Record\n5. Search Record\n6. Return")
                master_choice = input("Enter your choice: ")
                
                if master_choice == '1':
                    system.add_user()
                elif master_choice == '2':
                    system.display_users()
                elif master_choice == '6':
                    break
                else:
                    print("Invalid choice!")
        
        elif choice == '2':
            while True:
                print("1. Member Login\n2. Member Logout\n3. Non-Member Login\n4. Non-Member Logout\n5. Take Charges\n6. Show Charges\n7. Return")
                cafe_choice = input("Enter your choice: ")
                
                if cafe_choice == '1':
                    user_id = input("Enter User ID: ")
                    computer_id = input("Enter Computer ID: ")
                    system.book_computer(user_id, computer_id)
                elif cafe_choice == '2':
                    user_id = input("Enter User ID: ")
                    system.logout_computer(user_id)
                elif cafe_choice == '5':
                    user_id = input("Enter User ID: ")
                    system.calculate_charges(user_id)
                elif cafe_choice == '7':
                    break
                else:
                    print("Invalid choice!")
        
        elif choice == '3':
            system.save_data()
            print("Exiting...")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

