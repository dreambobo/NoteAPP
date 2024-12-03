import requests


def homepage_list(sid,userid,startindex=0,rows=0):
    homepage_note_list = []
    host = 'http://note-api.wps.cn'
    url = host + f'/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes'
    headers = {
        "cookie": f'wps_sid={sid}',
        "x-user-key": userid,
    }

    res = requests.get(url, headers=headers).json()['webNotes']
    for one in res:
        homepage_note_list.append(one['noteId'])
    return homepage_note_list

if __name__ == '__main__':
    print(homepage_list(userid='1281072265', sid='V02SFV_WGVWoA-YKBmvvbkQbZOY1slA00a6bef6e004c5b9c89'))