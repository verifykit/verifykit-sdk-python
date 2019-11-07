import requests
import json


class Verify:
    server_key = None
    response_body = {}
    is_valid = None
    api_version = "v1.0"
    api_url = "https://api.verifykit.com/"

    def __init__(self, server_key):
        self.server_key = server_key

    def is_valid(self):
        return self.is_valid

    def response(self):
        return self.response_body

    def validation(self, session_id):
        headers = {
            "X-Vfk-Server-Key": self.server_key
        }

        try:
            response = requests.post("{}{}/{}".format(self.api_url, self.api_version, 'result'), json={"sessionId": session_id}, headers=headers)

            if response.status_code == 200:
                self.is_valid = True
                self.response_body = json.loads(response.content)['result']
            else:

                self.is_valid = False

                response_body = response.json()['meta']

                self.response_body = {
                    'status': False,
                    'errorCode': response_body['errorCode'],
                    'errorMessage': response_body['errorMessage'],
                    'requestId': response_body['requestId'],
                }

        except Exception as e:

            self.is_valid = False
            response_body = response.json()['meta']
            self.response_body = {
                'status': False,
                'errorCode': response_body['errorCode'],
                'errorMessage': response_body['errorMessage'],
                'requestId': response_body['requestId'],
            }
