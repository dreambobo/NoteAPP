import unittest
import requests
import time

from parameterized import parameterized

from business_common.add_group import add_group
from business_common.del_note import del_note
from business_common.upload_note import upload_note
from common.generalAssert import GeneralAssert
from colorama import Fore
from common.caseMsgLogs import case, case_decorate, class_case_decoration, error, info
from business_common.business_requests import RequestCommon
from common.yamlRead import YamlRead


@class_case_decoration
class SetNoteGroupInput(unittest.TestCase):
    ga = GeneralAssert()
    re = RequestCommon()
    host = 'http://note-api.wps.cn'
    user_id = '1281072265'
    sid = 'V02SFV_WGVWoA-YKBmvvbkQbZOY1slA00a6bef6e004c5b9c89'
    api_config = YamlRead().data_config()['group_create']
    mustKeys = api_config['mustKeys']
    # group_id = str(int(time.time()) * 1000) + '_gid'

    def setUp(self) -> None:
        del_note(self.sid, self.user_id, del_group=True)

    @parameterized.expand(mustKeys)
    def testCase_must_key_remove(self,key):
        """必填项缺失"""
        host = 'http://note-api.wps.cn'
        url = host + '/v3/notesvr/set/notegroup'
        user_id = '1281072265'
        sid = 'V02SFV_WGVWoA-YKBmvvbkQbZOY1slA00a6bef6e004c5b9c89'
        headers = {
            "Cookie": f'wps_sid={sid}',
            "x-user-key": user_id,
            "Content-Type": "application/json"
        }

        body = {
            "groupId": str(int(time.time()) * 1000) + "_groupId",
            "groupName": "testGroup",
            "order": 0
        }

        body.pop(key)
        res = RequestCommon().post(url, headers=headers, body=body)
        response = res.json()
        expected = {'errorCode': -7, 'errorMsg': '参数不合法！'}
        self.assertEqual(500,res.status_code,msg='状态码校验失败')
        GeneralAssert().http_assert(expected,res.json())
