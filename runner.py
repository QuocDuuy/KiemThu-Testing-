# import unittest
# import HtmlTestRunner
# from test_chrome import *

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(automationChromeTest('testLogin'))
#     for i in range(3):
#         suite.addTest(automationChromeTest('testLoginUsernameError'))
#     suite.addTest(automationChromeTest('testLoginDifMethod'))
#     suite.addTest(automationChromeTest('testSearching'))
#     for i in range(2):
#         suite.addTest(automationChromeTest('testSearchingError'))
#     suite.addTest(automationChromeTest('testCheckBox'))

#     # Sử dụng HTMLTestRunner để tạo báo cáo
#     runner = HtmlTestRunner.HTMLTestRunner(output='reports')
#     runner.run(suite)
import unittest
import HtmlTestRunner
from module_runner import runChromeTests, runEdgeTests
from multiprocessing import Process

if __name__ == '__main__':

    # Tạo 2 quá trình độc lập để chạy các bộ thử nghiệm cho từng trình duyệt
    p1 = Process(target=runChromeTests)
    p2 = Process(target=runEdgeTests)

    # Bắt đầu chạy quá trình
    p1.start()
    p2.start()

    # Đợi cho quá trình kết thúc
    p1.join()
    p2.join()
