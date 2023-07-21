class account:
    def check_password_length(self, password):
        if len(password)>8:
            return True
        else:
            return False
if __name__=='__main__':
    accverify=account()
    print('The password length is '+str(accverify.check_password_length('iamaustinokariken'))

