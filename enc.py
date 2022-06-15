from cryptography.fernet import Fernet
message = "my deep dark secret".encode()

key = 'EqUsu_JEQl5KLTjhS6qcDpHRDhJHOTfEUT8foKVGXm8='

f = Fernet(key)
encrypted = f.encrypt(message)  # Encrypt the bytes. The returning object is of type bytes
print('the encrypted message is :\n')
print(encrypted.decode())

decrypted = f.decrypt(encrypted)
print('the decrypted message is :\n')
print(decrypted.decode())