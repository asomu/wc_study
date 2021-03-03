import requests


def ask_url():
    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (seperated by comma)")
    asked_url = input().split(',')
    asked_url = check_http(asked_url)


def check_url(asked_url):
    for url in asked_url:
        rg = requests.get(url).status_code
        if rg == requests.codes.ok:
            print(url + " is up!")
        else:
            print(url + " is Down!")


def check_http(asked_url):
    for i, url in enumerate(asked_url):
        if url.strip().startswith('http://'):
            continue
        else:
            asked_url[i] = 'http://' + url
            print(asked_url[i])
    check_url(asked_url)


if __name__ == '__main__':
    ask_url()
