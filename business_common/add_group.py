import time

import requests


def add_group(num,sid,userid):
    groupid_list = []
    for i in range(num):
        groupid = str(int(time.time() * 1000)) + '_gid'

        headers = {
            "cookie": f'wps_sid={sid}',
            "x-user-key": userid,
            "Content-Type": "application/json"
        }
        host = 'http://note-api.wps.cn'
        url = host + '/v3/notesvr/set/notegroup'
        body = {
            "groupId" : groupid,
            "groupName" : 'test',
            "order" : 0
        }

        res = requests.post(url,headers=headers,json=body)
        print(res.json())
        groupid_list.append(groupid)
    return groupid_list


if __name__ == '__main__':
    add_group(3, "V02SFV_WGVWoA-YKBmvvbkQbZOY1slA00a6bef6e004c5b9c89", "1281072265")