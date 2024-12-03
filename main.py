import unittest
import os
from BeautifulReport import BeautifulReport

DIR = os.path.dirname(os.path.abspath(__file__))
ENVIRON = 'Offline'  # 'Online' ->线上环境，'Offline' ->测试环境

if __name__ == '__main__':
    suite = unittest.TestLoader().discover('./testCase', "test*")
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    result = BeautifulReport(suite)
    result.report(filename='report.html',description='测试报告',report_dir='./')
