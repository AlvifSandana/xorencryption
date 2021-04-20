"""
Module: setup.py
Created by alvif@usagi 
on 20/04/21
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='xorencryption',
    packages=setuptools.find_packages(where="src"),
    version='0.1.5',
    license='MIT',
    description='little Python library for encrypt and decrypt using XOR operation.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alvif Sandana Mahardika',
    author_email='alvifsandana@gmail.com',
    url='https://github.com/AlvifSandana/xorencryption',
    download_url='https://github.com/AlvifSandana/xorencryption/',
    keywords=['XOR', 'LEARN', 'CRYPTOGRAPHY'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    package_dir={"": "src"},
    python_requires=">=3.7",
)
