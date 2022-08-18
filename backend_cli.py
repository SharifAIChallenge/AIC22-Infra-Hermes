import requests
from os import getenv


BACKEND_URL = getenv('BACKEND_URL')
BACKEND_STG_URL = getenv('BACKEND_STG_URL')
# BACKEND_URL = 'https://google.com'

print("backend client ready..")


class BackendCli:
    @staticmethod
    def send_event(data):
        try:
            result = requests.post(BACKEND_URL, json=data, headers={'Authorization': getenv('BACKEND_URL_TOKEN'), 'Content-Type': 'application/json; charset=utf-8'})
            result_stg = requests.post(BACKEND_STG_URL, json=data, headers={'Authorization': getenv('BACKEND_URL_TOKEN'), 'Content-Type': 'application/json; charset=utf-8'})
            # print(result.status_code, result.json(), 'prod',flush=True)
            try:
                print("--------- STG response: ", result_stg.status_code, result_stg.json(), flush=True)
                print("--------- PRD response: ", result.status_code, result.json(), flush=True)
            except Exception as error:
                print('ERROR --- ', data)
            return True
        except requests.exceptions.RequestException as e:
            print(e, flush=True)
            return False
