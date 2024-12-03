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

    def testCase001_handle_gethomepage_rows(self):
        """获取首页便签。
        handle：数值限制，当前用户存在2条便签，rows=1，查询首页便签
        预期：返回1条便签。"""
        info("创建2条便签")
        homepage_noteid = upload_note(2, self.userid, self.sid)
        case("获取首页便签,rows=1")
        startindex = 0
        rows = 1
        host = 'http://note-api.wps.cn'
        homepage_url = host + f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        res = RequestCommon().get(homepage_url, self.sid, self.userid)
        case(f'Received code : {res.status_code}')
        case(f'Received body : {res.json()}')
        # actural_res = []
        # for one in response:
        #     actural_res.append(one['noteId'])
        # for one in homepage_noteid:
        #     self.assertNotIn(one,actural_res)
        status_code = 200

        expected = {
            "responseTime": 0,
            "webNotes": [
                {
                    "noteId": homepage_noteid[1]['noteId'],
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
        GeneralAssert().http_assert(status_code, res.status_code)

    def testCase002_handle_gethomepage_startindx(self):
        """获取首页便签
        handle：数值限制；
        起始索引从1开始startindx：1，查询首页便签；
        预期：索引位置从1开始。
        """
        info("列表内构建2条数据")
        homepage_noteid = upload_note(2, self.userid, self.sid)
        startindex = 1
        rows = 0
        host = 'http://note-api.wps.cn'
        homepage_url = host + f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        res = RequestCommon.get(homepage_url, self.sid, self.userid)
        expected = {
            "responseTime": 0,
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

    def testCase003_handle_startindex_notExists(self):
        """获取首页便签
        startIndex字段缺失为None；
        预期：返回404。
        """
        info("列表内构建1条数据")
        homepage_noteid = upload_note(1, self.userid, self.sid)
        rows = 0
        host = 'http://note-api.wps.cn'
        homepage_url = host + f'/v3/notesvr/user/{self.userid}/home/startindex/rows/{rows}/notes'
        res = RequestCommon.get(homepage_url, self.sid, self.userid)
        self.assertEqual(404, res.status_code)
        self.assertIn('Not Found', res.json()['error'])

    def testCase004_handle_rows_noexists(self):
        """获取首页便签
        startIndex字段缺失为None；
        预期：返回404。
        """
        info("列表内构建1条数据")
        homepage_noteid = upload_note(1, self.userid, self.sid)
        startindex = 0
        host = 'http://note-api.wps.cn'
        homepage_url = host + f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/notes'
        res = RequestCommon.get(homepage_url, self.sid, self.userid)
        self.assertEqual(404, res.status_code)
        self.assertIn('Not Found', res.json()['error'])

    def testCase005_handle_extra_permission(self):
        """用户B获取用户A首页便签
        预期：返回401。
        """
        info("用户A列表内构建1条数据")
        homepage_noteid = upload_note(1, self.userid, self.sid)
        startindex = 0
        rows = 0
        host = 'http://note-api.wps.cn'
        homepage_url = host + f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        res = RequestCommon.get(homepage_url, self.sid_2, self.userid_2)
        expected = {
            "errorCode": -2010,
            "errorMsg": ""
        }
        self.assertEqual(401, res.status_code)
        GeneralAssert().http_assert(expected, res.json())

