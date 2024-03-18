import requests


class Connect():
    def __init__(self, url) -> None:
        self.url = url
    def ping():
        try:
            url = "http://127.0.0.1:8080/"
            response = requests.get(url)
            print(response.text)
        except Exception as e:
            print(f'Connection failed: {e}')
