# Cryptography

**Author:** Roman Sydoruk **Version:** 1.0.0

## Description

The application defines a method to encrypt a message that can then be decrypted when supplied with the corresponding key. Also there is a method to decipher the encrypted message event when you do NOT have the key.

## Architecture

* Python 3.8.3
* Poetry
* Pytest
* Regex

## Usage 
**read_file(path)** - the function takes data from text file and return a stripped string..\
**def encrypt** - the function takes a text and a key which is a numeric shift ('abc', 1) --> 'bcd'.\
**def decrypt** - the function takes an encrypted text and a key and decrypt a text('bcd', 1) --> 'abc'. \
**def print_all_versions** - the function takes an dencrypted text and store 26 versions into a list.\
**def decrypt_without_key** - the function takes an dencrypted text and encrypt it without a key.

[Link](https://github.com/sydoruk89/caesar-cipher)