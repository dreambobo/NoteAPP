import requests

from business_common.get_group import get_group
from business_common.homepage_list import homepage_list
from common.caseMsgLogs import info


def del_note(sid, userid, del_homepage=False, del_group=False, del_recycle=False):
    host = 'http://note-api.wps.cn'

    headers = {
        "cookie": f'wps_sid={sid}',
        "x-user-key": userid,
        "Content-Type": "application/json"
    }
    if del_homepage:
        url = host + '/v3/notesvr/delete'
        homepage_notid = homepage_list(userid='1281072265', sid='V02SFV_WGVWoA-YKBmvvbkQbZOY1slA00a6bef6e004c5b9c89')
        info("删除首页所有便签-完成")
        for one in homepage_notid:
            res = requests.post(url, headers=headers, json={"noteId": one})
            # print(res.json())
    if del_group:
        host = 'https://note-api.wps.cn'
        url = host + '/notesvr/delete/notegroup'
        group_list = get_group('1281072265', 'V02SFV_WGVWoA-YKBmvvbkQbZOY1slA00a6bef6e004c5b9c89')
        info("删除所有分组")
        for one in group_list:
            res = requests.post(url, headers=headers, json={"groupId": one})
            # print(res.json())
    if del_recycle:
        info("删除回收站下所有便签列表")
        url = host + '/v3/notesvr/cleanrecyclebin'
        res = requests.post(url, json={"noteIds": [-1]}, headers=headers)



if __name__ == '__main__':
    del_note(userid='1281072265', sid='V02SFV_WGVWoA-YKBmvvbkQbZOY1slA00a6bef6e004c5b9c89',
             del_homepage=True)
