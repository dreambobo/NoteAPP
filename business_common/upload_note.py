import time
import unittest

import requests


def upload_note(num, userid, sid, star=0, gropId=None, remindTime=None):
    """
    :param num: 构建个数
    :param userid: 用户id
    :param sid: 用户唯一标识
    :param star: 默认标星
    :param gropId: 组id
    :param remindTime: 提醒时间
    :return: 已创建的noteid
    """
    upload_noteid = []

    for i in range(num):
        host = 'http://note-api.wps.cn'
        upload_body_info_url = host + '/v3/notesvr/set/noteinfo'
        headers = {
            "cookie": f'wps_sid={sid}',
            "x-user-key": userid,
            "Content-Type": "application/json"
        }
        noteid = str(int(time.time() * 1000)) + '_nid'

        if remindTime:  # 日历便签
            upload_body_info = {
                "noteId": noteid,
                "remindTime": remindTime,
                "remindType": 0,
                "star": 0
            }

        if gropId:  # 分组便签
            upload_body_info = {
                "noteId": noteid,
                "groupId": gropId,
                "star": 0
            }
        else:  # 普通便签
            upload_body_info = {
                "noteId": noteid,
                "star": 0
            }

        res = requests.post(upload_body_info_url, headers=headers, json=upload_body_info)

        upload_content_url = host + '/v3/notesvr/set/notecontent'
        upload_content_body = {
            "noteId": noteid,
            "title": "test",
            "summary": "test",
            "body": "test",
            "localContentVersion": 1,
            "BodyType": 1
        }
        res_contnt = requests.post(upload_content_url, headers=headers, json=upload_content_body)
        response = res_contnt.json()
        upload_noteid.append(upload_content_body)
    return upload_noteid


if __name__ == '__main__':
    print(upload_note(1, "1281072265", "V02SFV_WGVWoA-YKBmvvbkQbZOY1slA00a6bef6e004c5b9c89"))