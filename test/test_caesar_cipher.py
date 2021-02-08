import pytest
from caesar_cipher.caesar_cipher import encrypt, decrypt, crack



 
def test_encrypt():
    actual = encrypt('abc', 3)
    expected = 'def'
    assert actual == expected

def test_decrypt():
    actual = decrypt('def', 3)
    expected = 'abc'
    assert actual == expected

def test_encrypt_upper_case():
    actual = encrypt('Abc', 3)
    expected = 'Def'
    assert actual == expected

def test_encrypt_character_white_space():
    actual = encrypt('abc!.', 3)
    expected = 'def!.'
    assert actual == expected

def test_crack():
    test = encrypt('It was the best of times, it was the worst of times. ', 3)
    actual = crack(test)
    expected = 'It was the best of times, it was the worst of times. '
    assert actual == expected   

