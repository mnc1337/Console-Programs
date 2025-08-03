import requests
import json


def pause(message: str) -> None:
    print(message)
    input("Press Enter to close this tab... ")


def url_exists(url: str) -> bool:
    try:
        response = requests.head(url, allow_redirects=True, timeout=0.5)
        if response.status_code == 405:
            response = requests.get(url, allow_redirects=True, timeout=0.5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def send_request() -> None:
    try:
        CONSTANTS = {
            "URL_PATTERN": "protocol://domain:port/",
            "URL_PATTERN_EXPLANATION": {
                "protocol": "http / https",
                "domain": "127.0.0.1 (localhost) / google.com",
                "port": "any number in range: [0; 65536] if not taken by another process",
            },
            "METHODS": ["GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"],
            "MIN_NUMBER_OF_REQUESTS": 1,
            "MAX_NUMBER_OF_REQUESTS": 1000,
            "JSON_STRING_EXAMPLE": "{\"key\": \"value\", ...} (\"...\" means that there can be many \"key\": \"value\" pairs)"
        }

        METHODS_LIST = CONSTANTS["METHODS"]
        METHODS_STRING = ", ".join(METHODS_LIST)
        URL_PATTERN = CONSTANTS["URL_PATTERN"]
        PATTERN_EXPLANATION = CONSTANTS["URL_PATTERN_EXPLANATION"]
        MIN_NUMBER_OF_REQUESTS = CONSTANTS["MIN_NUMBER_OF_REQUESTS"]
        MAX_NUMBER_OF_REQUESTS = CONSTANTS["MAX_NUMBER_OF_REQUESTS"]
        JSON_STRING_EXAMPLE = CONSTANTS["JSON_STRING_EXAMPLE"]

        while True:
            successful_counter = 0
            operations_number = 3

            url = input(f"Enter URL to send request to (in format \"{URL_PATTERN}\"): ").strip()
            if url_exists(url):
                successful_counter += 1
            else:
                print(f"Entered URL was not found or unreachable.\nExplanation:\n{PATTERN_EXPLANATION}\n")

            method = input(f"Enter request method ({METHODS_STRING}): ").strip().upper()
            if method in METHODS_LIST:
                successful_counter += 1
            else:
                print(f"Incorrect method. Should be one of: {METHODS_STRING}")

            try:
                number_of_requests = int(input(f"Enter number of requests ({MIN_NUMBER_OF_REQUESTS}-{MAX_NUMBER_OF_REQUESTS}): "))
                if MIN_NUMBER_OF_REQUESTS <= number_of_requests <= MAX_NUMBER_OF_REQUESTS:
                    successful_counter += 1
                else:
                    print(f"Invalid number. It should be in the range: [{MIN_NUMBER_OF_REQUESTS}; {MAX_NUMBER_OF_REQUESTS}]\n")
            except ValueError:
                print("Invalid input. Please enter an integer.")

            if successful_counter == operations_number:
                for i in range(1, number_of_requests + 1):
                    try:
                        if method == "GET":
                            response = requests.get(url, allow_redirects=True, timeout=0.5)
                            print()
                            if response.status_code == 404:
                                print(f"[STATUS 404] Entered resource was not found ({url}). Details are below:\n")
                            elif response.status_code == 405:
                                print(f"[STATUS 405] Method {method} is not allowed at {url}. Details are below:\n")
                            elif response.status_code == 429:
                                print(f"[STATUS 429] Url {url} has a limit for sending requests. Details are below:\n")

                        elif method == "HEAD":
                            response = requests.head(url, allow_redirects=True, timeout=0.5)
                            print()
                            if response.status_code == 404:
                                print(f"[STATUS 404] Entered resource was not found ({url}). Details are below:\n")
                            elif response.status_code == 405:
                                print(f"[STATUS 405] Method {method} is not allowed at {url}. Details are below:\n")
                            elif response.status_code == 429:
                                print(f"[STATUS 429] Url {url} has a limit for sending requests. Details are below:\n")

                        elif method == "OPTIONS":
                            response = requests.options(url, allow_redirects=True, timeout=0.5)
                            print()
                            if response.status_code == 404:
                                print(f"[STATUS 404] Entered resource was not found ({url}). Details are below:\n")
                            elif response.status_code == 405:
                                print(f"[STATUS 405] Method {method} is not allowed at {url}. Details are below:\n")
                            elif response.status_code == 429:
                                print(f"[STATUS 429] Url {url} has a limit for sending requests. Details are below:\n")

                        elif method == "POST":
                            json_data = input(f"\n[Request #{i}] Enter data in JSON format (or leave empty for empty body): ").strip()
                            try:
                                data = json.loads(json_data) if json_data else {}
                            except json.JSONDecodeError:
                                print(f"Invalid JSON. It should be like next: {JSON_STRING_EXAMPLE}. Skipping request #{i}.")
                                continue
                            response = requests.post(url, json=data, allow_redirects=True, timeout=0.5)
                            if response.status_code == 404:
                                print(f"\n[STATUS 404] Entered resource was not found ({url}). Details are below:\n")
                            elif response.status_code == 405:
                                print(f"\n[STATUS 405] Method {method} is not allowed at {url}. Details are below:\n")
                            elif response.status_code == 429:
                                print(f"\n[STATUS 429] Url {url} has a limit for sending requests. Details are below:\n")

                        elif method == "PUT":
                            json_data = input(f"\n[Request #{i}] Enter data in JSON format (or leave empty for empty body): ").strip()
                            try:
                                data = json.loads(json_data) if json_data else {}
                            except json.JSONDecodeError:
                                print(f"Invalid JSON. It should be like next: {JSON_STRING_EXAMPLE}. Skipping request #{i}.")
                                continue
                            response = requests.put(url, json=data, allow_redirects=True, timeout=0.5)
                            if response.status_code == 404:
                                print(f"\n[STATUS 404] Entered resource was not found ({url}). Details are below:\n")
                            elif response.status_code == 405:
                                print(f"\n[STATUS 405] Method {method} is not allowed at {url}. Details are below:\n")
                            elif response.status_code == 429:
                                print(f"\n[STATUS 429] Url {url} has a limit for sending requests. Details are below:\n")
                        
                        elif method == "PATCH":
                            json_data = input(f"\n[Request #{i}] Enter data in JSON format (or leave empty for empty body): ").strip()
                            try:
                                data = json.loads(json_data) if json_data else {}
                            except json.JSONDecodeError:
                                print(f"Invalid JSON. It should be like next: {JSON_STRING_EXAMPLE}. Skipping request #{i}.")
                                continue
                            response = requests.patch(url, json=data, allow_redirects=True, timeout=0.5)
                            if response.status_code == 404:
                                print(f"\n[STATUS 404] Entered resource was not found ({url}). Details are below:\n")
                            elif response.status_code == 405:
                                print(f"\n[STATUS 405] Method {method} is not allowed at {url}. Details are below:\n")
                            elif response.status_code == 429:
                                print(f"\n[STATUS 429] Url {url} has a limit for sending requests. Details are below:\n")
                        
                        elif method == "DELETE":
                            response = requests.delete(url, allow_redirects=True, timeout=0.5)
                            print()
                            if response.status_code == 404:
                                print(f"[STATUS 404] Entered resource was not found ({url}). Details are below:\n")
                            elif response.status_code == 405:
                                print(f"[STATUS 405] Method {method} is not allowed at {url}. Details are below:\n")
                            elif response.status_code == 429:
                                print(f"[STATUS 429] Url {url} has a limit for sending requests. Details are below:\n")

                        else:
                            print(f"{method} method is invalid or is not supported by this program. Supported methods: {METHODS_STRING}")
                            break

                        content_type = response.headers.get("Content-Type", "")
                        is_json = "application/json" in content_type

                        request_and_response_data = {
                            "request": {
                                "number": i,
                                "method": method,
                            },
                            "response": {
                                "status_code": response.status_code,
                                f"{method}_data": response.json() if is_json else response.text,
                            }
                        }

                        print(json.dumps(request_and_response_data, indent=2))
                        
                    except requests.exceptions.RequestException as e:
                        print(f"\nRequest #{i} failed with error: {e}")

                if method in METHODS_LIST:
                    print(f"\nSent {number_of_requests} request{'s' if number_of_requests > 1 else ''} to {url} using method {method}.\n")
            
            else:
                unsuccessful_counter = operations_number - successful_counter
                print(f"At least one entered value is invalid. Details: {unsuccessful_counter} out of {operations_number} operation{'s' if operations_number != 1 else ''} had invalid argument{'s' if unsuccessful_counter != 1 else ''}.")

            while True:
                again = input("Do you want to try again? (y/n): ").strip().lower()
                if again == "y":
                    break
                elif again == "n":
                    pause("Further execution was rejected by user.")
                    return
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

    except KeyboardInterrupt:
        pause("\nProgram execution was aborted by user.")


if __name__ == "__main__":
    send_request()