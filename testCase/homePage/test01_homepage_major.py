import time
import unittest

import requests

from business_common.business_requests import RequestCommon
from business_common.del_note import del_note
from business_common.homepage_list import homepage_list
from business_common.upload_note import upload_note
from common.caseMsgLogs import info, class_case_decoration, case
from common.generalAssert import GeneralAssert
from business_common import business_requests


@class_case_decoration
class TestHomePage(unittest.TestCase):
    userid = '1281072265'
    sid = 'V02SFV_WGVWoA-YKBmvvbkQbZOY1slA00a6bef6e004c5b9c89'
    groupid = str(int(time.time() * 1000)) + '_gid'
    userid_2 = '1281072264'
    sid_2 = 'V02SFV_WGVWoA-YKBmvvbkQbZOY1slA00a6bef6e004c5b9c90'

    def setUp(self) -> None:
        info("用例初始化，清理首页便签数据")
        del_note(self.sid, self.userid, del_homepage=True)

    def testCase001_major(self):
        """获取首页便签列表_主流程"""
        rows = 0
        startindex = 0
        info("创建首页1条便签")
        homepage_noteid = upload_note(1, self.userid, self.sid)
        info("获取首页便签列表")
        host = 'http://note-api.wps.cn'
        homepage_url = host + f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        res = RequestCommon().get(homepage_url, self.sid, self.userid)
        expected = {
            "responseTime": int,
            "webNotes": [
                {
                    "noteId": homepage_noteid[0]['noteId'],
                    "createTime": int,
                    "star": 0,
                    "remindTime": 0,
                    "remindType": 0,
                    "infoVersion": 1,
                    "infoUpdateTime": int,
                    "groupId": None,
                    "title": "test",
                    "summary": "test",
                    "thumbnail": None,
                    "contentVersion": 1,
                    "contentUpdateTime": int
                }
            ]
        }
        GeneralAssert().http_assert(expected, res.json())