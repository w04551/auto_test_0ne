from common import HTMLTestRunner_cn
import unittest
import os
# start_dir = "D:\\xuexi13\\testproject\\case"

curdir = os.path.dirname(os.path.realpath(__file__))
print(curdir)
start_dir = os.path.join(curdir, "case")
print(start_dir)
discover = unittest.defaultTestLoader.discover(start_dir,
                                               pattern="test*.py")
print(discover)


# report_path = "D:\\xuexi13\\testproject\\report\\result.html"

report_path = os.path.join(curdir, "report", "result.html")
print(report_path)

fp = open(report_path, "wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                          title="测试报告的title",
                                          description="测试报告的描述,当前时间",
                                          retry=1)
runner.run(discover)
fp.close()

# with open(report_path, "wb") as fp:
#     runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
#                                               title="测试报告的title",
#                                               description="测试报告的描述,当前时间",
#                                               retry=1)
#     runner.run(discover)