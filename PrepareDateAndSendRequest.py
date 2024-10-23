import requests
import Server1

class PrepareDateAndSendRequest:
    def __init__(self):
        pass
    
    def getDataFromServer1(self):
        server1 = Server1.Server1()
        return server1.getData()

    def prepareData(self):
        data = self.getDataFromServer1()
        data["d"].append("newData") 
        return data
    
    def sendRequest(self, sendData):
        url = "https://test.com/api/v1/testapi"
        params = {'data': sendData}
        # sending get request and saving the response as response object
        r = requests.get(url = url, params = params)

        # extracting data in json format
        # Sample: {result: True}
        response = r.json()  
        return response

    def prepareDateAndSendRequest(self):
        return self.sendRequest(self.prepareData())
