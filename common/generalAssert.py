import unittest
from common.caseMsgLogs import error

class GeneralAssert(unittest.TestCase):
    # def http_assert(self,expected,actual):
    """
    http 返回体通用的断言方法
    :param expected: 期望值 | dict or list,接口返回体的预期值
    :param actual: 实际值 | dict or list, 实际结果获取方式通常可以用 response.json()
    :return: True断言成功， Fail 断言失败
    """

    '''a_actural = [
    {
        "userId": "1281072265",
        "groupId": "1731941866000_gid",
        "groupName": "test",
        "order": 0,
        "valid": 1,
        "updateTime": 1731941866353
    },
    {
        "userId": "1281072265",
        "groupId": "1731941892000_gid",
        "groupName": "test",
        "order": 0,
        "valid": 1,
        "updateTime": 1731941893102
    }
],'''

    def http_assert(self, expected, actural):
        if isinstance(expected, dict):
            self.assertEqual(len(expected.keys()), len(actural.keys()))
            for key, value in expected.items():
                self.assertIn(key, actural.keys())
                if isinstance(value, type):
                    self.assertEqual(value, type(actural[key]))
                elif isinstance(value, list):
                    self.assertEqual(len(value), len(actural[key]))
                    for index in range(len(value)):
                        # self.assertEqual(len(value)),len(actural[key])
                        if isinstance(value[index], type):
                            self.assertEqual(value[index], type(actural[key][index]))
                        elif isinstance(value[index], dict):
                            self.http_assert(value[index], actural[key][index])
                        else:
                            self.assertEqual(value[index], actural[key][index])

                else:
                    self.assertEqual(value, actural[key])
        elif isinstance(expected, list):
            self.assertEqual(len(expected),len(actural))
            for index in range(len(expected)):
                self.assertEqual(expected[index],actural[index])
                if isinstance(expected[index],type):
                    self.http_assert(expected[index], type(actural[index]))
                elif isinstance(expected[index],dict):
                    self.http_assert(expected[index],actural[index])
                elif isinstance(expected[index],list):
                    self.http_assert(expected[index],actural[index])
                else:
                    self.assertEqual(expected[index], actural[index])
        else:
            self.assertEqual(expected,actural)
    '''expected = {'responseTime': 0, 'webNotes': ["a","b",[0,9],{"a":"b"}]}'''
    '''actural = [{'responseTime': 0, 'webNotes': ["a","b",[0,9],{"a":"b"}]}'''

    # def http_assert(self,expected,actural):
    #     if isinstance(expected,dict):
    #         self.assertEqual(len(expected.keys()),len(actural.keys()))
    #         for key,value in expected.items():
    #             self.assertIn(key,actural.keys())
    #             if isinstance(value,type):
    #                 self.assertEqual(value,type(actural[key]))
    #
    #             elif isinstance(value, list):
    #                 self.assertEqual(len(value),len(actural(value)))
    #                 for index in range(len(value)):
    #                     if isinstance(value[index],type):
    #                         self.assertEqual(value[index],type(actural[key][index]))
    #                     elif isinstance(value, dict):
    #                         self.http_assert(value[index], actural[key][index])
    #                     else:
    #                         self.assertEqual(value[index], actural[key][index])
    #             else:
    #                 self.assertEqual(value,actural[key])
    #     else:
    #         self.assertEqual(len(expected),len(actural))
    #
    #         for index in range(len(expected)):
    #             if isinstance(expected[index], type):
    #                 self.assertEqual(expected[index],type(actural[index]))
    #             elif isinstance(expected[index],dict):
    #                 self.http_assert(expected[index],actural[index])
    #             elif isinstance(expected[index], list):
    #                 self.http_assert(expected[index], actural[index])
    #             else:
    #                 self.assertEqual(expected[index], actural[index])

    # def new_assert_True(self,expected,msg=None):
    #     if not expected:
    #         error(f'assertFail expect:{expected}')
    #         self.fail(None)
