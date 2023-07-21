import unittest
import account as AccounntClass
class Test(unittest.TestCase):
    accInfo=AccounntClass.account()
    def test_check_password_length(self):
        print('checking possible passowrds')
        passwordList=['andrwbjbdw', 'jjwvkks', 'bisbsibwibisbws']
        for password in passwordList:
            print('checking for '+password)
            passInfo=self.accInfo.check_password_length(password)
            self.assertTrue(passInfo)
if __name_=='__main__':
    unittest.main()
