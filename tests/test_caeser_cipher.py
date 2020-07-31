from caeser_cipher import __version__
from caeser_cipher.caeser_cipher import encrypt, decrypt, decrypt_without_key


def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    assert encrypt('hello', 1) == 'ifmmp'
    assert decrypt('ifmmp', 1) == 'hello'
    assert encrypt('Hello Jonh', 30) == 'Lipps Nsrl'
    assert encrypt('Hi, $, !&', 9) == 'Qr, $, !&'
    encrypted = encrypt('It was the best of times, it was the worst of times.', 19)
    assert decrypt_without_key(encrypted) == ' It was the best of times, it was the worst of times.'