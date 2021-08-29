from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import assertionTest
from searches import searchesTest


assertion_test = TestLoader().loadTestsFromTestCase(assertionTest)
search_test = TestLoader().loadTestsFromTestCase(searchesTest)

smoke_test = TestSuite([assertion_test, search_test])

kwargs = {
    'output': 'smoke_report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)