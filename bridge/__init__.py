from requests import post, get


class BridgeManager:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def upload(self, content):
        post(
            url=self.baseUrl + '/api/v1/firmware/upload',
            json=dict(content=content)
        )

    def getLog(self):
        return get(
            url=self.baseUrl + '/api/v1/firmware/log'
        ).json()['log']