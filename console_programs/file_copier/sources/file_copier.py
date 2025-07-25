import os
import shutil
import time
from datetime import datetime


def pause(message: str = ""):
    if message:
        print(message)
    input("Press Enter to continue... ")


def perform_copy():
    start_path = input("Enter a start path: ").strip()
    if not os.path.exists(start_path):
        pause("Error: Start path does not exist.")
        return

    print(f"Selected start path: {start_path}\n")

    end_path = input("Enter an end path: ").strip()
    if os.path.isfile(start_path) and os.path.isdir(end_path):
        pass
    elif os.path.isdir(start_path) and os.path.isfile(end_path):
        pause("Error: Cannot copy a directory into a file path.")
        return
    elif not os.path.exists(os.path.dirname(end_path)) and not os.path.isdir(end_path):
        pause("Error: Destination parent directory does not exist.")
        return

    print(f"Selected end path: {end_path}\n")

    try:
        interval = float(input("Enter copying interval in seconds (1–600): "))
        if not (1 <= interval <= 600):
            pause("Error: Interval must be between 1 and 600 seconds.")
            return
    except ValueError:
        pause("Value Error: Entered value is not a valid number.")
        return

    try:
        while True:
            timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

            if os.path.isfile(start_path):
                full_end_path = (
                    os.path.join(end_path, os.path.basename(start_path))
                    if os.path.isdir(end_path)
                    else end_path
                )
                shutil.copy2(start_path, full_end_path)
                print(f"[{timestamp}] File copied: {start_path} -> {full_end_path}")

            elif os.path.isdir(start_path):
                if os.path.exists(end_path):
                    shutil.rmtree(end_path)
                shutil.copytree(start_path, end_path)
                print(f"[{timestamp}] Directory copied: {start_path} -> {end_path}")

            time.sleep(interval)

    except PermissionError:
        pause("Permission Error: One of the paths is inaccessible.")
    except OSError as err:
        pause(f"System Error: {str(err)}")


def main():
    incorrect_answers_counter = 0
    while True:
        if not incorrect_answers_counter:
            perform_copy()
        answer = input("Do you want to perform another copy task? (y/n): ").strip().lower()
        if answer == "y":
            incorrect_answers_counter = 0
            continue
        elif answer == "n":
            print("Continuing was rejected. Exiting program.")
            time.sleep(1.5)
            break
        else:
            print("Answer is incorrect.")
            incorrect_answers_counter += 1
            continue


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram execution was interrupted by the user.")
        pause()
