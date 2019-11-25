# content of ./test_smtpsimple.py
import pytest


@pytest.fixture
def smtp_connection():
    import smtplib 

    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5) #smtplib.SMTP() instance created by the fixture function. Ex: smtp_connection = <smtplib.SMTP instance at 0x000000000409F0C8>


def test_ehlo(smtp_connection): #In the failure traceback we see that the test function was called with a smtp_connection argument
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0  # for demo purposes