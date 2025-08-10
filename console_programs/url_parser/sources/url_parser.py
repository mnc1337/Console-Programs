from bs4 import BeautifulSoup
from collections import Counter
import requests
import time
import rich
import json


def pause(message: str, without_message: bool = False) -> None:
    if without_message:
        input("Press Enter to close this tab... ")
    else:
        print(message)
        input("Press Enter to close this tab... ")


def url_exists(url: str) -> bool:
    try:
        response = requests.head(url, allow_redirects=True, timeout=0.5)
        if response.status_code == 405:
            response = requests.get(url, allow_redirects=True, timeout=0.5)
        return response.ok
    except requests.exceptions.RequestException:
        return False


def handle_html(response):
    rich.print("\n[bold]Data type: HTML[/bold]")
    time.sleep(1)

    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup.find_all(True)
    tags_list = [f"<{tag.name}>" for tag in tags]
    tags_counter = Counter(tags_list)
    sorted_tags_count = tags_counter.most_common()
    unique_tags = sorted(tags_counter.keys())

    time.sleep(0.5)
    rich.print("\n[bold]Tags:[/bold]")
    time.sleep(0.5)
    for tag in unique_tags:
        time.sleep(0.25)
        print(tag)

    time.sleep(0.5)
    rich.print("\n[bold]Tags count:[/bold]")
    time.sleep(0.5)
    for tag, count in sorted_tags_count:
        time.sleep(0.25)
        print(f"{tag}: {count}")

    time.sleep(0.5)
    most_common_tag, occurrences = sorted_tags_count[0]
    rich.print(f"\n[bold]Total number of tags: {len(tags_list)}[/bold]")
    rich.print(f"[bold]Most common tag: {most_common_tag} - number of occurrences: {occurrences}.[/bold]\n")


def handle_json(response):
    rich.print("\n[bold]Data type: JSON[/bold]")
    time.sleep(0.5)

    json_data = response.json()
    formatted_json_data = json.dumps(json_data, indent=4)

    rich.print("\n[bold]Data:[/bold]")
    time.sleep(0.5)

    if isinstance(json_data, (list, dict)):
        if isinstance(json_data, dict):
            iterable = json_data.items()
            description = "{key: value} pairs"
        else:
            iterable = enumerate(json_data, start=1)
            description = "elements in list"

        for key, value in iterable:
            time.sleep(0.25)
            print(f"{key}: {value}")

        rich.print(f"\n[bold]Total number of objects: {len(json_data)} ({description}).[/bold]\n")
    else:
        print(formatted_json_data + "\n")


def parse_url():
    ALLOWED_CONTENT_TYPES = ["text/html", "application/json"]
    ALLOWED_CONTENT_TYPES_STRING = ", ".join(ALLOWED_CONTENT_TYPES)

    try:
        while True:
            url = input("Enter a URL to parse (or type 'exit' to quit): ").lower().strip()
            if url == "exit":
                pause("", without_message=True)
                break

            if not url_exists(url):
                print("The entered URL does not exist or is unreachable.")
                continue

            try:
                response = requests.get(url, allow_redirects=True, timeout=1)
                content_type = response.headers.get("Content-Type", "").lower()

                if "text/html" in content_type:
                    handle_html(response)

                elif "application/json" in content_type:
                    handle_json(response)

                else:
                    print(f"Parsed URL does not return content of type: {ALLOWED_CONTENT_TYPES_STRING}.")

            except Exception as e:
                print(f"An exception occurred: {e}")

    except KeyboardInterrupt:
        pause("\nProgram executing aborted by user.")


if __name__ == "__main__":
    parse_url()