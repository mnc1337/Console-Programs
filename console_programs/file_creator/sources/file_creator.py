"""
Copyright (c) 2025 mnc1337.
This file is distributed under the MIT License.
See the LICENSE file for details.
"""

"""
Notification:
The `tempfile` module can also be used to get the TEMP directory (e.g., via `tempfile.gettempdir()`), 
and it’s less vulnerable to environment variable changes than os.environ.
"""

import os
import tempfile


def create_test_files(directory: str) -> None:
    try:
        while True:
            try:
                iters_num = int(input("Enter number of files to create (1–1000) or 0 to exit: "))
            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 1000.")
                continue

            if iters_num == 0:
                print("Goodbye! Thanks for using this program.")
                input("Press Enter to close this tab... ")
                break

            if not (1 <= iters_num <= 1000):
                print("Number must be between 1 and 1000.")
                continue

            try:
                for i in range(iters_num):
                    full_path = os.path.join(directory, f"test_{i}.txt")
                    with open(full_path, "w", encoding="utf-8") as file:
                        file.write("test")
                print(f"{iters_num} file{'s' if iters_num > 1 else ''} {'have' if iters_num > 1 else 'has'} been successfully created in: {directory}")
            except PermissionError:
                print("Permission denied. Cannot write to the specified directory.")
    except KeyboardInterrupt:
        print("\nProgram was aborted by user.")
        input("Press Enter to close this tab... ")


if __name__ == "__main__":
    create_test_files(directory=tempfile.gettempdir())
