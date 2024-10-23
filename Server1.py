class Server1:
    def __init__(self):
        pass

    def getData(self):
        url = "https://server1.com/api/v1/testapi"
        raise Exception(f"Cannot connect server {url}")
        