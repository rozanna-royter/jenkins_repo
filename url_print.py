import requests
import os


def main():
    url_list = os.environ['URLS'].split(',')
    for url in url_list:
        print(f"====== Printing contents of: ${url} ======")
        r = requests.get(url)
        print(r.text)


if __name__ == "__main__":
    main()
