import pytest
import login

def test_empty(self):
    "Test empty username and password "
    assert login.login('', '') == False
def test_success(self):
    "Test correct username and password"
    assert login.login('admin', 'admin') == True
def test_fail(self):
    "Test username password case sensitivity"
    assert login.login('ADmin', 'adMin') == False
def test_multiple_attempts(self):
    "Test lockout after three failed attempts"
    login.login('admin', 'test')
    login.login('admin', 'test')
    login.login('admin', 'test')
    assert login.login('admin', 'admin') == False