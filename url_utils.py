import requests

def get_url_status_codes(urls: list[str]) -> dict[str, int | None]:
  """
  Fetches the HTTP status code for a list of URLs.

  Args:
    urls: A list of URL strings.

  Returns:
    A dictionary mapping each URL to its status code.
    If an error occurs while fetching a URL, the value for that URL will be None.
  """
  status_codes_map: dict[str, int | None] = {}
  for url in urls:
    try:
      response = requests.get(url, timeout=5)
      status_codes_map[url] = response.status_code
    except requests.exceptions.RequestException:
      status_codes_map[url] = None
  return status_codes_map

if __name__ == "__main__":
    example_urls = [
        "https://www.google.com",
        "https://www.github.com",
        "http://thisurldoesnotexist.invalidtld",
        "https://httpstat.us/200",
        "https://httpstat.us/404",
        "https://httpstat.us/500"
    ]
    print("Fetching status codes for example URLs:")
    results = get_url_status_codes(example_urls)
    for url, status in results.items():
        print(f"{url}: {status}")
