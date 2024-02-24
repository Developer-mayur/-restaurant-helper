import random
import re
from datetime import datetime

def is_valid_date_of_birth(date_of_birth):
    try:
        day, month, year = map(int, date_of_birth.split('/'))
        if not (1 <= day <= 31 and 1 <= month <= 12 and year >= 1900):
            return False
    except ValueError:
        return False
    return True

def is_valid_mobile_number(mobile_number):
    if len(mobile_number) == 10 and mobile_number.startswith('0') and mobile_number.isdigit():
        return True
    return False

def is_valid_password(password):
    pattern = r'^[a-zA-Z][\w@&]*\d$'
    if re.match(pattern, password):
        return True
    return False

def is_21_years_old(date_of_birth):
    today = datetime.now()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    return age >= 21

def sign_up():
    user_info = {}
    user_info["name"] = input("Enter your Full Name: ")
    user_info["email"] = input("Enter your email address: ")

    while True:
        date_of_birth = input("Please enter your date of birth (DD/MM/YYYY): ")
        if is_valid_date_of_birth(date_of_birth):
            dob = datetime.strptime(date_of_birth, "%d/%m/%Y")
            if not is_21_years_old(dob):
                print("You must be at least 21 years old to sign up.")
                continue
            else:
                user_info["date_of_birth"] = dob
                break
        else:
            print("Invalid date of birth format. Please enter in DD/MM/YYYY format.")

    while True:
        mobile_number = input("Please enter your mobile number: ")
        if is_valid_mobile_number(mobile_number):
            user_info["mobile_number"] = mobile_number
            break
        else:
            print("Invalid mobile number. It must be 10 digits starting with 0.")

    while True:
        password = input("Enter your password: ")
        if is_valid_password(password):
            confirm_password = input("Re-enter your password: ")
            if password == confirm_password:
                user_info["password"] = password
                break
            else:
                print("Password confirmation does not match. Please try again.")
        else:
            print("Invalid password format. It must start with alphabets, followed by either '@' or '&' and end with a numeric.")

    return user_info

def sign_in(users):
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    for user_info in users.values():
        if user_info["email"] == email and user_info["password"] == password:
            return user_info
    return None



def reset_password(users):
    email = input("Enter your email address: ")
    for user_id, user_info in users.items():
        if user_info["email"] == email:
            oldpassword = input("Enter your old password: ")
            if user_info["password"] != oldpassword:
                print("Incorrect old password.")  
            else:
                while True:
                    password = input("Enter your new password: ")
                    if not is_valid_password(password):
                        print("Your password is not strong enough.")
                        continue
                    repassword = input("Re-enter your new password: ")
                    if password != repassword:
                        print("Your new password and re-entered password do not match.")
                        continue
                    if password == oldpassword:
                        print("New password cannot be the same as the old password.")
                        continue
                    user_info["password"] = password
                    print("Password reset successful!")
                    return
        else:
            continue
    print("User not found.")


def main():
    users = {}
    while True:
        print("\nPlease select an option:")
        print("1. Sign up")
        print("2. Sign in")
        print("3. Reset Password")
        print("4. Quit")
        choice = input("Enter your choice: \n")

        if choice == "1":
            new_user = sign_up()   
            users[random.randint(10000, 99999)] = new_user
            print("Sign up successful")

        elif choice == "2":
            user_info = sign_in(users)
            if user_info:
                print("Welcome back, " + user_info["name"] + "!")
            else:
                print("Invalid email address or password.")

        elif choice == "3":
            reset_password(users)

        elif choice == "4":
            print("Thank you for using the application!")
            break

        elif choice == "5":
            print("\nUsers:")
            for user_id, user_info in users.items():
                print("User ID:", user_id)
                print("Name:", user_info["name"])
                print("Email:", user_info["email"])
                print()  # Add a blank line for better readability

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
