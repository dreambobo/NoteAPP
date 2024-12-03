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

    def testCase_major(self):
        """新增分组接口，主流程：用户新增分组"""
        info("用户A请求新增分组接口,构建1个分组数据")
        group_list = add_group(1, self.sid, self.user_id)
        print(group_list)
        info("分组数据下创建1个便签")
        upload_noteid = upload_note(1, self.sid, self.user_id, gropId=group_list[0])
        info("获取分组列表")
        url = self.host + '/v3/notesvr/get/notegroup'
        body = {"excludeInValid": True}
        res = RequestCommon().post(url,body,sid=self.sid,userid=self.user_id)

        expected = {
            "noteGroups": [
                {
                    "userId": self.user_id,
                    "groupId": group_list[0],
                    "groupName": "test",
                    "order": 0,
                    "valid": 1,
                    "updateTime": int
                }
            ],
            "requestTime": int
        }

        self.assertEqual(200, res.status_code, msg='状态码断言失败')
        GeneralAssert().http_assert(expected, res.json())


