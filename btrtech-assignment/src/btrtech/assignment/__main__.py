"""The entry point to our CLI.

Feel free to rewrite the whole file if you need to. The only expected (and mandatory)
symbol here is a callable named ``entry`` (declared in ``pyproject.toml``).
Most of the following functions have been badly written on purpose, to encourage
you to rewrite everything in your own style instead.
You only need to comply with the ``README.md``, especially the functionalities
described under ``Task``. As long as your CLI accepts all the arguments and options,
it's fine.

Please note that the provided CLI **does not** fully comply with the requested task.

You can even rewrite / remove this docstring here.
"""

import os
import sys
import requests

DEFAULT_SERVER_URL: str = "http://localhost"
DEFAULT_SERVER_PORT: int = 80

def request_url(target_url: str) -> str:
    """Execute an HTTP GET request to a target URL."""
    try:
        response = requests.get(target_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error making HTTP request to {target_url}: {e}")
        raise  # Reraise the exception for the caller to handle



def write_to_file(data: str, file_path: str) -> None:
    """Write data to a file."""
    try:
        with open(file_path, "w") as file:
            file.write(data)
        print(f"Data successfully written to {file_path}")
    except OSError as e:
        print(f"Error writing to file {file_path}: {e}")
        raise  # Reraise the exception for the caller to handle



def main(max_events: int, max_time: int, target_server: str, output_file: str) -> None:
    """Retrieve data from the server and write it to a file."""
    try:
        data = request_url(target_server)
        write_to_file(data, output_file)
    except Exception as e:
        print(f"Error processing events: {e}")
        sys.exit(1)


def entry():
    """Entry point function."""
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <maxEvents> <maxTime>")
        sys.exit(1)

    max_events = int(sys.argv[1])
    max_time = int(sys.argv[2])

    target_server = os.getenv("BTRTECH_SERVER_URL", f"{DEFAULT_SERVER_URL}:{DEFAULT_SERVER_PORT}")
    output_file = "output.json"  # Default output file

    main(max_events, max_time, target_server, output_file)


if __name__ == "__main__":
    entry()