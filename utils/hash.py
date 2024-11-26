from hashlib import sha256

password = 'Andriy'

crypto_password = sha256(password.encode('utf-8')).hexdigest()

print(crypto_password) 