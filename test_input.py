__author__ = 'ALEX'
import unittest
import BankAccountFiles

class input_test_case(unittest.TestCase):
    def runTest(self):
        self.failIf(BankAccountFiles.file_write("fox"))

def suite():

    suite = unittest.TestSuite()

    suite.addTest (input_test_case())

    return suite

if __name__== '__main__':
    runner = unittest.TextTestRunner()

    test_suite = suite()

    runner.run (test_suite)

