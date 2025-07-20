"""
Copyright (c) 2025 mnc1337.
This file is distributed under the MIT License.
See the LICENSE file for details.
"""

import os
import time
import tempfile
from send2trash import send2trash


def delay(seconds: float) -> None:
    if seconds > 0:
        time.sleep(seconds)


def clear_pycache() -> None:
    for elem in os.scandir(os.getcwd()):
        if elem.is_dir() and elem.name == "__pycache__":
            send2trash(elem.path)


def program_aborting() -> None:
    print("\nProgram running was aborted by user.")
    input("Press Enter to close this window... ")


def ask_confirmation(directory: str) -> bool:
    while True:
        answer = input(
            f"Directory for temporary files: {directory}.\n"
            f"Program will clean this directory. Do you want to continue? (y/n): "
        ).strip().lower()
        answers = ["y", "n"]
        if answer in answers:
            return answer == "y"
        print("Please enter 'y' or 'n'.")


def clean_directory(directory: str) -> None:
    os.chdir(directory)
    contents = os.listdir()

    if not ask_confirmation(directory):
        print("Continuing was rejected by user.")
        input("Press Enter to close this window... ")
        return

    print(f"Checking directory: {directory}")

    deleted_counter = 0
    locked_counter = 0

    for content in contents:
        if content.startswith("_MEI"): # Temporary build directory of PyInstaller
            continue
        try:
            send2trash(os.path.join(directory, content))
            deleted_counter += 1
        except PermissionError:
            locked_counter += 1

    delay(1)
    if deleted_counter == 0:
        print("No objects were sent to the trash bin.")
    else:
        print(f"Objects sent to the trash bin: {deleted_counter}")

    if locked_counter:
        delay(1)
        print(f"Objects locked by other processes: {locked_counter}")

    delay(0.5)
    print("Program finished successfully.")
    input("Press Enter to close this window... ")


def get_temp_path() -> str | None:
    return tempfile.gettempdir()


def run() -> None:
    try:
        clear_pycache()
        temp_dir = get_temp_path()
        if temp_dir:
            clean_directory(temp_dir)
        else:
            print("TEMP path not found in environment variables.")
            input("Press Enter to close this window... ")
    except KeyboardInterrupt:
        program_aborting()


if __name__ == "__main__":
    run()
