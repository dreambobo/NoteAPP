import requests
from common.caseMsgLogs import info, error, case
from common.yamlRead import YamlRead


class RequestCommon():
    @staticmethod
    def post(url, body, sid=None, userid=None, headers=None):
        if headers is None:
            headers = {
                "cookie": f'wps_sid={sid}',
                "x-user-key": userid,
                "Content-Type": "application/json"
            }
        info(f'Request url: {url}')
        info(f'Request headers :{headers}')
        info(f'Request body : {body}')
        try:
            res = requests.post(url, headers=headers, json=body, timeout=5)
        except TimeoutError:
            error(f"当前url地址:{url}请求超时")
            return 'Request TimeOut!'
        info(f'Received code : {res.status_code}')
        info(f'Received body : {res.json()}')
        return res

    @staticmethod
    def get(url, sid=None, userid=None,headers=None):
        if headers is None:
            headers = {
                "cookie": f'wps_sid={sid}',
                "x-user-key": userid
            }


        info(f'Request url: {url}')
        info(f'Request headers :{headers}')
        try:
            res = requests.get(url,headers = headers,timeout=5)
        except TimeoutError:
            error(f"当前url地址:{url}请求超时")
            return 'Request TimeOut!'
        info(f'Received code : {res.status_code}')
        info(f'Received body : {res.json()}')
        return res