import unittest
import HtmlTestRunner
from test_chrome import *
from test_edge import *
import os

def runChromeTests():
    suite = unittest.TestSuite()
    suite.addTest(automationChromeTest('testLogin'))
    for _ in range(3):
        suite.addTest(automationChromeTest('testLoginUsernameError'))
    suite.addTest(automationChromeTest('testLoginDifMethod'))
    suite.addTest(automationChromeTest('testSearching'))
    for _ in range(2):
        suite.addTest(automationChromeTest('testSearchingError'))
    suite.addTest(automationChromeTest('testCheckBox'))
    # Sử dụng HTMLTestRunner để tạo báo cáo

    store_path = "D:/University/Testing/sources"
    os.chdir(store_path)
    runner = HtmlTestRunner.HTMLTestRunner(output='reports_chrome')
    runner.run(suite)

def runEdgeTests():
    suite = unittest.TestSuite()
    suite.addTest(automationEdgeTest('testLogin'))
    for _ in range(3):
        suite.addTest(automationEdgeTest('testLoginUsernameError'))
    suite.addTest(automationEdgeTest('testLoginDifMethod'))
    suite.addTest(automationEdgeTest('testSearching'))
    for _ in range(2):
        suite.addTest(automationEdgeTest('testSearchingError'))
    suite.addTest(automationEdgeTest('testCheckBox'))
    # Chạy các bộ thử nghiệm trên Edge
    store_path = "D:/University/Testing/sources"
    os.chdir(store_path)
    runner = HtmlTestRunner.HTMLTestRunner(output='reports_edge')
    runner.run(suite)
