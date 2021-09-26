# XOR Encryption
[![Total alerts](https://img.shields.io/lgtm/alerts/g/AlvifSandana/xorencryption.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/AlvifSandana/xorencryption/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/AlvifSandana/xorencryption.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/AlvifSandana/xorencryption/context:python) 

XOR Encryption is a little Python library for encrypt and decrypt string with key. 
This library is for those of you who are learning encryption using the XOR method.

### How it Works
The library uses a simple encryption algorithm that converts plain text and keys to binary form and then XORs them both to generate cipher text.
Here's the mathematical notation:

![XOR encryption notation ](http://www.sciweavers.org/tex2img.php?eq=C%20%3D%20P%20%5Coplus%20K%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

Because performing XOR operations with the same value twice in a row yields the original value, the following is the mathematical notation for decryption:

![XOR decryption notation](http://www.sciweavers.org/tex2img.php?eq=P%20%3D%20C%20%5Coplus%20K%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

Note:
 - P = Plain text 
 - K = Key
 - C = Cipher text

### How to Use
Example code:

```
from xorencryption import XOREncryption

plain = "this is your plain text"
key = "boom"
enc = XOREncryption()

enc.set_plaintext(plaintext=plain)
enc.set_key(key=key)

print(enc.encrypt())  # return cipher text
print(enc.decrypt())  # return decrypted text
```


