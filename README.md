# URL Status Checker

This project provides a Python script (`url_utils.py`) with a function to check the HTTP status codes for a list of URLs.

## Features

-   Takes a list of URLs as input.
-   Fetches each URL using an HTTP GET request.
-   Returns a dictionary mapping each URL to its HTTP status code.
-   Handles errors gracefully: if a URL cannot be reached or an error occurs during the request, its status code in the returned dictionary will be `None`.

## Files

-   `url_utils.py`: Contains the main function `get_url_status_codes` and an example usage block.
-   `test_url_utils.py`: Contains unit tests for the `get_url_status_codes` function.

## `get_url_status_codes` function

The core of this utility is the `get_url_status_codes(urls)` function.

-   **Input**: `urls` (list of strings) - A list of URLs to check.
-   **Output**: `dict` - A dictionary where keys are the URLs and values are their corresponding HTTP status codes. If a request fails for a specific URL, the value for that URL will be `None`.

## Prerequisites

This script requires the `requests` library. You can install it using pip:

```bash
pip install requests
```

## Usage

### 1. Running the script directly

You can run `url_utils.py` directly to see an example of its output with a predefined list of URLs:

```bash
python url_utils.py
```

This will print the status codes for the example URLs defined in the `if __name__ == "__main__":` block of the script.

### 2. Importing into your own Python code

To use the function in your own project:

```python
from url_utils import get_url_status_codes

my_urls = ["https://www.example.com", "http://another-site.org"]
status_results = get_url_status_codes(my_urls)

for url, status in status_results.items():
    print(f"The status for {url} is {status}")
```

## Running Tests

Unit tests are provided in `test_url_utils.py`. To run the tests, navigate to the root directory of the project in your terminal and run:

```bash
python -m unittest test_url_utils.py
```
