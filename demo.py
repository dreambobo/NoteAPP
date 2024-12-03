import time
import requests

user_id = '1281072265'
sid = 'V02SFV_WGVWoA-YKBmvvbkQbZOY1slA00a6bef6e004c5b9c89'
host = 'http://note-api.wps.cn'

url = host + '/v3/notesvr/set/notegroup'
headers = {
    "Cookie": f'wps_sid={sid}',
    "x-user-key": user_id,
    "Content-Type": "application/json"
}
group_id = str(int(time.time()) * 1000) + '_gid'
body = {
    "groupId": group_id,
    "groupName": "test",
    "order": 0
}
res = requests.post(url, headers=headers, json=body)

assert res.status_code == 200
assert "responseTime" in res.json().keys()
assert "updateTime" in res.json().keys()
assert 2 == len(res.json().keys())
assert type(res.json()['responseTime']) == int
assert type(res.json()['updateTime']) == int

get_url = host + '/v3/notesvr/get/notegroup'
body = {"excludeInValid": True}
res = requests.post(get_url, headers=headers, json=body)
assert len(res.json()['noteGroups']) == 1
assert res.json()['noteGroups'][0]['groupId'] == group_id
