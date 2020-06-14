import requests
import os


def main():
    url_list = os.environ['URLS'].split(',')
    # url_list = ['http://www.youtube.com','http://www.facebook.com','http://www.baidu.com','http://www.yahoo.com','http://www.amazon.com']
    for url in url_list:
        r = requests.get(url)
        print(r.text)


if __name__ == "__main__":
    main()
