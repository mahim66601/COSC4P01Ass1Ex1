import authentication

class TestLogin:
    def test_empty(self):
        "Test empty username and password "
        assert authentication.User.login(authentication.User,'', '') == False
    def test_success(self):
        "Test correct username and password"
        assert authentication.User.login(authentication.User,'admin', 'admin') == True
    def test_fail(self):
        "Test username password case sensitivity"
        assert authentication.User.login(authentication.User,'ADmin', 'adMin') == False
    def test_multiple_attempts(self):
        "Test lockout after three failed attempts"
        authentication.User.login(authentication.User,'admin', 'test')
        authentication.User.login(authentication.User,'admin', 'test')
        authentication.User.login(authentication.User,'admin', 'test')
        assert authentication.User.login(authentication.User,'admin', 'admin') == False