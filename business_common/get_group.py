import requests


def get_group(userid,sid,excludeInValid=True):
    group_list = []
    host = 'http://note-api.wps.cn'
    url = host + '/v3/notesvr/get/notegroup'
    headers = {
        "cookie": f'wps_sid={sid}',
        "x-user-key": userid,
        "Content-Type": "application/json"
    }
    body = {
        "excludeInValid":excludeInValid
    }
    res = requests.post(url,headers=headers,json=body).json()['noteGroups']
    for one in res:
        group_list.append(one['groupId'])
    return group_list

if __name__ == '__main__':
    print(get_group('1281072265', 'V02SFV_WGVWoA-YKBmvvbkQbZOY1slA00a6bef6e004c5b9c89'))