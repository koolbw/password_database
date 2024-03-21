# Symmetric key encryption 

# from cryptography.fernet import Fernet

# message = "password123"

# key = Fernet.generate_key()
# fernet = Fernet(key)
# encMessage = fernet.encrypt(message.encode()) 

# print("original string: ", message)
# print("encrypted string: ", encMessage)

# decMessage = fernet.decrypt(encMessage).decode()
 
# print("decrypted string: ", decMessage)


# Asymmetric key encryption

import rsa

publicKey, privateKey = rsa.newkeys(512)
print(publicKey)
print()
print(privateKey)

message = "thisIsMyPassword123!"


encMessage = rsa.encrypt(message.encode(), 
						publicKey)

print("original string: ", message)
print("encrypted string: ", encMessage)


decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("decrypted string: ", decMessage)
