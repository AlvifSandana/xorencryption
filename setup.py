"""
Module: setup.py

Created by alvif@usagi 
on 20/04/21
"""
from distutils.core import setup
setup(
  name='XORENCRYPTION',         # How you named your package folder (MyLib)
  packages=['XORENCRYPTION'],   # Chose the same as "name"
  version='0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description='TYPE YOUR DESCRIPTION HERE',   # Give a short description about your library
  author='ALVIF SANDANA MAHARDIKA',                   # Type in your name
  author_email='alvifsandana@gmail.com',      # Type in your E-Mail
  url='https://github.com/AlvifSandana/enc_dec_xor',   # Provide either the link to your github or to your website
  download_url='https://github.com/AlvifSandana/enc_dec_xor/v_01.tar.gz',    # I explain this later on
  keywords=['XOR', 'LEARN', 'CRYPTOGRAPHY'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Encryption',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
  ],
)