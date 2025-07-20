"""
Copyright (c) 2025 mnc1337.
This file is distributed under the MIT License.
See the LICENSE file for details.
"""

def main():
    import random, os
    from datetime import datetime

    print("It's a console program that generates passwords according to given parameters.")

    while True:
        password = ""
        chars_for_password = ""

        try:
            # Defining password length
            while True:
                user_input = input("Enter password length (8-32) or 'exit': ").strip()
                if user_input.lower() == "exit":
                    print("Goodbye!")
                    input("Press Enter key to exit... ")
                    return
                if not user_input.isdigit():
                    print("Input is not a number or it starts with special char(or chars). Try again.")
                    continue

                password_length = int(user_input)
                if 8 <= password_length <= 32:
                    break
                else:
                    print("Length must be from 8 to 32.")

            # Defining chars type
            while True:
                choices = [
                    (1, "Only numbers"),
                    (2, "Only uppercase chars"),
                    (3, "Only lowercase chars"),
                    (4, "All variants")
                ]
                print("Available character sets:")
                for num, desc in choices:
                    print(f"{num}. {desc}")
                choice_input = input("Choose character type or 'exit': ").strip()

                if choice_input.lower() == "exit":
                    print("Goodbye!")
                    input("Press Enter key to exit... ")
                    return
                if not choice_input.isdigit():
                    print("Input is not a number or it starts with special char(or chars). Try again.")
                    continue

                choice_num = int(choice_input)
                if choice_num == 1:
                    chars_for_password = "0123456789"
                    break
                elif choice_num == 2:
                    chars_for_password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    break
                elif choice_num == 3:
                    chars_for_password = "abcdefghijklmnopqrstuvwxyz"
                    break
                elif choice_num == 4:
                    chars_for_password = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                    break
                else:
                    print("Invalid option. Try again.")

            # Generating password
            password = ''.join(random.choice(chars_for_password) for _ in range(password_length))
            print(f"Generated password: {password}")

            while True:
                file_path = input("Enter path (or 'exit' to cancel). If only file name is entered, file will be saved to the same directory as this program: ").strip()
                if file_path.lower() == "exit":
                    print("Password saving was cancelled.")
                    break

                if not file_path.endswith(".txt"):
                    file_path += ".txt"

                dir_name = os.path.dirname(file_path) or "."
                if not os.path.isdir(dir_name):
                    create_dir = input("Directory does not exist. Create it? (Y/N): ").strip().upper()
                    if create_dir == "Y":
                        try:
                            os.makedirs(dir_name, exist_ok=True)
                            print(f"Directory was created successfully: {dir_name}")
                        except PermissionError:
                            print("Permission denied. Cannot create directory.")
                            continue
                        except OSError as e:
                            print(f"Path creation error: {str(e)}")
                            continue
                    elif create_dir == "N":
                        print("Directory not created.")
                        continue
                    else:
                        print("Invalid input. Please enter Y or N.")
                        continue

                try:
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(f"Password: {password}\n")
                        file.write(f"Created at: {datetime.now()}")
                    print("Password saved successfully.")
                    break
                except Exception as e:
                    print(f"File error: {e}")
                    continue


            # Requesting to repeat
            while True:
                repeat = input("Generate another password? (Y/N): ").strip().upper()
                if repeat == "Y":
                    break
                elif repeat == "N":
                    print("OK. Goodbye! Thanks for using this program!")
                    input("Press Enter key to exit... ")
                    return
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")
        
        except KeyboardInterrupt:
            print("\nProgram was interrupted by user.")
            input("Press Enter key to exit... ")
            return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram was terminated by user.")
