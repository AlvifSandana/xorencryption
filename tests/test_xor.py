r""" Unittest for module `xor.py` in `xorencrytion package`
Usage:
$ python tests\test_xor.py
"""

# import xorencryption package from src directory
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from xorencryption import XOREncryption
import random
import unittest

class TestXOR(unittest.TestCase):
    def setUp(self):
        self.enc = XOREncryption()
    
    @staticmethod
    def random_plain_text(length=20) -> str:
        """
        Return a random string of plain text of len `length=20`.
        Contains ASCII characters from 'A' (65) -> 'Z' (90)
        
        :param data: length (int) Defaults to 20.

        :return: str
        """
        return ''.join([chr(random.randint(65, 90)) for _ in range(length)])
    
    @staticmethod
    def random_key(length=10) -> str:
        """
        Return a random string of key of len `length=10`.
        Contains ASCII characters from 'A' (65) -> 'Z' (90)
        
        :param data: length (int) Defaults to 10.

        :return: str
        """
        return TestXOR.random_plain_text(length=length)
    
    def test_binary_to_decimal(self):
        """Unittest for method `XOREncryption.binary_to_decimal`"""
        binary_list = ['0b00110001', '0b00100010', '0b00111000']
        int_list = [49, 34, 56]
        
        self.assertEqual(self.enc.binary_to_decimal(binary_list), int_list)
    
    def test_decimal_to_ascii(self):
        """Unittest for method `XOREncryption.decimal_to_ascii`"""
        int_list = [65, 66, 67]
        string = 'ABC'
        
        self.assertEqual(self.enc.decimal_to_ascii(int_list), string)
    
    def test_encrypt_decrypt(self):
        """Unittest for method `XOREncryption.encrypt` and `XOREncryption.decrypt`"""
        for _ in range(100):
            # generate a random string of plain text and key
            plain_text:str = self.random_plain_text()
            key:str = self.random_key()
            # checking the setter and getter methods
            self.enc.set_plaintext(plaintext=plain_text)
            self.enc.set_key(key=key)
            
            cipher:str = self.enc.encrypt()
            
            # checking the constructor
            decipher:str = XOREncryption(key=key, ciphertext=cipher).decrypt()
            
            self.assertEqual(plain_text, decipher)
            
   
if __name__ == '__main__':
    unittest.main()