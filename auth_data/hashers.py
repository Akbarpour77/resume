from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth.hashers import MD5PasswordHasher


class MyPBKDF2PasswordHasher(MD5PasswordHasher):
    """
    A subclass of MD5PasswordHasher that uses 100 times more iterations.
    """
    iterations = MD5PasswordHasher.iterations * 100
