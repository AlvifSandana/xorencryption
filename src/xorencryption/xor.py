"""
Module: xor.py
Created by alvif@usagi 
on 20/04/21
"""
class XOREncryption:
    def __init__(self, plaintext="", key="", ciphertext=""):
        self.__plaintext = plaintext
        self.__ciphertext = ciphertext
        self.__key = key

    def set_plaintext(self, plaintext: str):
        """
        Set plain text value

        :param plaintext: str
        """
        self.__plaintext = plaintext

    def get_plaintext(self):
        """
        Get plain text value

        :rtype: str
        """
        return self.__plaintext

    def set_key(self, key: str):
        """
        Set key value

        :param key: str
        """
        self.__key = key

    def get_key(self):
        """
        Get key value.

        :rtype: str
        """
        return self.__key

    def set_ciphertext(self, ciphertext: str):
        """
        Set cipher text value

        :param ciphertext: str
        """
        self.__ciphertext = ciphertext

    def get_ciphertext(self):
        """
        Get cipher text value

        :rtype: str
        """
        return self.__ciphertext

    @staticmethod
    def __generate_bytearray(data=''):
        """
        Generate bytearray from input data (data as string)

        :param data: string
        :return: bytearray from input data
        """
        return bytearray(data, encoding='utf-8')

    @staticmethod
    def __generate_binary(data):
        """
        Generate list of binary from input data (data as bytearray)

        :param data: bytearray
        :return: list
        """
        generated = []
        list_tmp = []
        for byte in data:
            tmp = bin(byte).replace('0b', '')
            if len(tmp) < 8:
                tmp = '0' * (8 - len(tmp)) + tmp
                for b in tmp:
                    list_tmp.append(int(b))
            else:
                for b in tmp:
                    list_tmp.append(int(b))
            generated.append(list_tmp)
            list_tmp = []
        return generated

    @staticmethod
    def __generate_xor_list(plain_text_bin_list: list, key_bin_list: list) -> list:
        """

        :param plain_text_bin_list:
        :param key_bin_list:
        :return:
        """
        generated_xor_list = []
        tmp = []
        i = 0
        j = 0
        for ld in plain_text_bin_list:
            for d in ld:
                tmp.append(d ^ key_bin_list[i][j])
                j += 1
            i = (i + 1) % len(key_bin_list)
            j = 0
            generated_xor_list.append(tmp)
            tmp = []
        return generated_xor_list

    @staticmethod
    def __join_xor(xor_list: list) -> list:
        """
        Join elements of list that represents binary value
        to the list of binary.
        Example: [[0, 1, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1]] to
        ['0b01001011', '0b01000001']

        :param xor_list: list
        :return: list
        """
        xor_bin = []
        tmp = []
        for d in xor_list:
            for lst in d:
                tmp.append(str(lst))
            tmp1 = ''.join(tmp)
            xor_bin.append('0b' + tmp1)
            tmp = []
        return xor_bin

    @staticmethod
    def binary_to_decimal(data: list) -> list:
        """
        Convert list of binary to the list of decimal.
        Example: ['0b00110001', '0b00100010', '0b00111000'] => [49, 34, 56]

        :param data: list of binary
        :return: list of decimal
        """
        decimal = []
        for d in data:
            decimal.append(int(d, 2))
        return decimal

    @staticmethod
    def decimal_to_ascii(data: list) -> str:
        """
        Convert elements of number list to string.
        Example: [65, 66, 67] => "ABC"

        :param data: list of number (integer)
        :return: string
        """
        list_enc = []
        for d in data:
            list_enc.append(chr(d))
        enc_text = ''.join(list_enc)
        return enc_text

    def encrypt(self):
        """
        Encrypt string by convert each plain text and key character to binary
        then do XOR operation between binary plain text and key.

        :return: str
        """
        try:
            # plain text and key
            plain_text = self.__plaintext.upper()
            key = self.__key

            # Generate bytearray from plain text and key
            bytearray_pt = self.__generate_bytearray(plain_text)
            bytearray_k = self.__generate_bytearray(key)

            # Generate binary from plain text and key
            list_bin_pt = self.__generate_binary(bytearray_pt)
            list_bin_k = self.__generate_binary(bytearray_k)

            # Do xor operation between binary value
            # of the plain text and key
            xor_bin_list = self.__generate_xor_list(list_bin_pt, list_bin_k)

            # xor bin
            xor = self.__join_xor(xor_bin_list)

            # Convert binary to decimal
            dec = self.binary_to_decimal(xor)

            # Decimal to ASCII
            encrypted = self.decimal_to_ascii(dec)
            return encrypted
        except Exception as e:
            print(e)

    def decrypt(self):
        """
        Decrypt cipher text by convert each characters (also key) to binary
        then do XOR operation between binary cipher text and key.

        :return: str
        """
        try:
            # plain text and key
            cipher_text = self.__ciphertext.upper()
            key = self.__key

            # Generate bytearray from plain text and key
            bytearray_pt = self.__generate_bytearray(cipher_text)
            bytearray_k = self.__generate_bytearray(key)

            # Generate binary from plain text and key
            list_bin_pt = self.__generate_binary(bytearray_pt)
            list_bin_k = self.__generate_binary(bytearray_k)

            # Do xor operation between binary value
            # of the plain text and key
            xor_bin_list = self.__generate_xor_list(list_bin_pt, list_bin_k)

            # xor bin
            xor = self.__join_xor(xor_bin_list)

            # Convert binary to decimal
            dec = self.binary_to_decimal(xor)

            # Decimal to ASCII
            decrypted = self.decimal_to_ascii(dec)
            return decrypted
        except Exception as e:
            print(e)
