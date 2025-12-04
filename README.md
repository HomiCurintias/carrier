Carrier

Carrier is a very small and simple data storage library.
It uses plain text files with the .carrier extension to store key–value pairs.

The goal of Carrier is not to replace JSON, SQLite, or any complex format.
It exists for situations where you just want something extremely lightweight:
a readable file, a simple structure, and a few functions to write and read data.

Carrier is intentionally minimal. It is meant to stay in the background of your code, not be the central focus of your project.

How it works

A .carrier file is just a text file with entries in the following format:

key:
    value
another_key:
    another value


Each key ends with a colon, and the value appears on the next line with a leading tab character.

The library provides functions to create files, append new fields, update existing fields, and read values.

Basic Usage
import carrier

Create a new .carrier file

This overwrites the file if it already exists.

carrier.ncar("user.carrier", "password", "1234")


This produces:

password:
    1234

Read a value
value = carrier.body("user.carrier", "password")
print(value)


body() automatically attempts to convert the value to an integer if possible.

Append a new key to an existing file
carrier.apd("user.carrier", "age", 19)


Result:

password:
    1234
age:
    19

Change an existing value
carrier.cng("user.carrier", "password", "newpass")


This updates only the value, keeping the same key.

Practical Example

Below is a minimal example showing how Carrier can be used in a simple login-like system.

import carrier
import hashlib

def hash_password(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Save a user
carrier.ncar("john.carrier", "password", hash_password("123"))

# Read and compare
saved = carrier.body("john.carrier", "password")

if saved == hash_password("123"):
    print("Logged in")
else:
    print("Wrong password")


This demonstrates how Carrier fits naturally into a real program. It behaves similarly to JSON or INI files: a simple, small utility for storing data.

Functions
ncar(file, key, value)

Creates (or replaces) a .carrier file and writes a single key–value pair.

apd(file, key, value)

Appends a new key–value pair to the end of the file.

body(file, key)

Reads the value of the given key.
Returns "Not found" if the key does not exist.

cng(file, key, value)

Changes the value of an existing key without altering any others.
