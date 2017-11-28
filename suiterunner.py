from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from tests.tests import TestForm
from tests.validations import ValidateForm
import os


form_tests = TestLoader().loadTestsFromTestCase(TestForm)
form_validations = TestLoader().loadTestsFromTestCase(ValidateForm)

suite = TestSuite([form_tests, form_validations])

outfile = os.pardir + '\\test-reports'
runner = HTMLTestRunner(output=outfile)

runner.run(suite)
